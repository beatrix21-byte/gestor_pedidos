from clientes import clientes
from utilidades import pedir_numero


class LineaPedido:
    """Representa una línea individual de un pedido.
    
    Encapsula un producto con su precio y cantidad, proporcionando
    métodos para calcular el subtotal de esa línea específica.
    
    Attributes:
        producto (str): Nombre o descripción del producto.
        precio (float): Precio unitario del producto.
        cantidad (int): Cantidad de unidades solicitadas.
    
    Raises:
        ValueError: Si se intenta calcular el subtotal con cantidad <= 0.
    """
    
    def __init__(self, producto, precio, cantidad):
        """Inicializa una nueva línea de pedido.
        
        Args:
            producto (str): Nombre o descripción del producto.
            precio (float): Precio unitario del producto.
            cantidad (int): Cantidad de unidades solicitadas.
        
        Examples:
            >>> linea = LineaPedido("Teclado", 25.0, 2)
            >>> linea.producto
            'Teclado'
        """
        self.producto = producto
        self.precio = precio
        self.cantidad = cantidad
    
    def subtotal(self):
        """Calcula el subtotal de la línea de pedido.
        
        Multiplica el precio unitario por la cantidad. Valida que
        la cantidad sea mayor a 0 antes del cálculo.
        
        Returns:
            float: El subtotal (precio * cantidad).
        
        Raises:
            ValueError: Si la cantidad es menor o igual a 0.
        
        Examples:
            >>> linea = LineaPedido("Ratón", 10.0, 2)
            >>> linea.subtotal()
            20.0
        """
        if self.cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que 0")
        return self.precio * self.cantidad


class Pedido:
    """Representa un pedido completo con validación y cálculos.
    
    Agrupa múltiples líneas de pedido para un cliente específico,
    proporcionando métodos para gestionar las líneas y calcular
    el total con descuentos aplicados automáticamente.
    
    Attributes:
        nombre_cliente (str): Nombre del cliente que realiza el pedido.
        lineas (list): Lista de objetos LineaPedido que componen el pedido.
        estado (str): Estado actual del pedido (por defecto "pendiente").
    """
    
    def __init__(self, nombre_cliente):
        """Inicializa un nuevo pedido.
        
        Args:
            nombre_cliente (str): Nombre del cliente que realiza el pedido.
        
        Examples:
            >>> pedido = Pedido("Ana")
            >>> pedido.nombre_cliente
            'Ana'
            >>> pedido.estado
            'pendiente'
        """
        self.nombre_cliente = nombre_cliente
        self.lineas = []
        self.estado = "pendiente"
    
    def agregar_linea(self, linea):
        """Agrega una línea de producto al pedido.
        
        Args:
            linea (LineaPedido): La línea de pedido a agregar.
        
        Returns:
            None
        
        Examples:
            >>> pedido = Pedido("Ana")
            >>> linea = LineaPedido("Silla", 100.0, 2)
            >>> pedido.agregar_linea(linea)
            >>> len(pedido.lineas)
            1
        """
        self.lineas.append(linea)
    
    def total_con_descuento(self):
        """Calcula el total del pedido con descuentos automáticos.
        
        Suma todos los subtotales de las líneas y aplica un descuento
        según las reglas de negocio: 15% si >= 200€, 10% si > 100€.
        
        Returns:
            float: El total del pedido después de aplicar descuentos.
        
        Examples:
            >>> pedido = Pedido("Ana")
            >>> pedido.agregar_linea(LineaPedido("Silla", 100.0, 2))
            >>> pedido.total_con_descuento()
            170.0
        """
        subtotal = calcular_total_lineas(self.lineas)
        descuento = calcular_descuento(subtotal)
        return subtotal - descuento


def calcular_total_lineas(lineas):
    """Calcula el total sumando todos los subtotales de las líneas.
    
    Args:
        lineas (list): Lista de objetos LineaPedido a sumar.
    
    Returns:
        float: La suma de todos los subtotales de las líneas.
    
    Examples:
        >>> lineas = [LineaPedido("Ratón", 10.0, 2), LineaPedido("Monitor", 150.0, 1)]
        >>> calcular_total_lineas(lineas)
        170.0
    """
    return sum(linea.subtotal() for linea in lineas)


def calcular_descuento(total):
    """Calcula el descuento aplicable según el monto total.
    
    Aplica descuentos progresivos:
    - 15% si el total es >= 200€
    - 10% si el total es > 100€
    - 0% en otros casos
    
    Args:
        total (float): El monto total antes de descuento.
    
    Returns:
        float: El importe del descuento a aplicar.
    
    Examples:
        >>> calcular_descuento(150.0)
        15.0
        >>> calcular_descuento(300.0)
        45.0
        >>> calcular_descuento(50.0)
        0.0
    """
    if total >= 200:
        return total * 0.15
    elif total > 100:
        return total * 0.10
    return 0.0


pedidos = []


def menu_pedidos():
    """Muestra el menú interactivo de gestión de pedidos.
    
    Presenta un menú con opciones para crear, listar, calcular
    totales de pedidos y volver al menú principal. El menú se
    repite hasta que el usuario elige salir.
    
    Returns:
        None
    
    Side Effects:
        Imprime menú en consola y modifica la lista global 'pedidos'.
    """
    fin = False
    while fin == False:
        print("\n--- PEDIDOS ---")
        print("1. Crear pedido")
        print("2. Listar pedidos")
        print("3. Calcular total de un pedido")
        print("4. Volver")
        opcion = input("Opción: ")

        if opcion == "1":
            nuevo_pedido()
        elif opcion == "2":
            ver_pedidos()
        elif opcion == "3":
            calcular_total_desde_menu()
        elif opcion == "4":
            fin = True
        else:
            print("Opción incorrecta")


def nuevo_pedido():
    """Crea un nuevo pedido interactivamente.
    
    Guía al usuario a través del proceso de creación de un pedido:
    selecciona un cliente, agrega líneas de productos con cantidad
    y precio, y finalmente guarda el pedido en la lista global.
    
    Returns:
        None
    
    Side Effects:
        Modifica la lista global 'pedidos' agregando un nuevo pedido.
    """
    print("\nCREAR PEDIDO")
    if len(clientes) == 0:
        print("Primero debes crear un cliente")
        return

    i = 0
    while i < len(clientes):
        print(str(i + 1) + ". " + clientes[i]["nombre"])
        i = i + 1

    numero_cliente = pedir_numero("Elige cliente: ")
    if numero_cliente < 1 or numero_cliente > len(clientes):
        print("Cliente incorrecto")
        return

    lineas = []
    seguir = "s"
    while seguir == "s":
        producto = input("Producto: ")
        cantidad = pedir_numero("Cantidad: ")
        precio = float(input("Precio unidad: "))

        if producto == "":
            print("Producto vacío")
        elif cantidad <= 0:
            print("Cantidad incorrecta")
        elif precio <= 0:
            print("Precio incorrecto")
        else:
            lineas.append({"producto": producto, "cantidad": cantidad, "precio": precio})
            print("Línea añadida")

        seguir = input("¿Añadir otro producto? s/n: ")

    pedido = {"cliente": clientes[numero_cliente - 1], "lineas": lineas, "estado": "pendiente"}
    pedidos.append(pedido)
    print("Pedido creado")


def ver_pedidos():
    """Muestra el listado completo de pedidos con sus totales.
    
    Imprime un listado numerado de todos los pedidos registrados,
    mostrando el cliente, estado y total con descuentos aplicados.
    Si no hay pedidos, muestra un mensaje informativo.
    
    Returns:
        None
    
    Side Effects:
        Imprime información en la consola.
    """
    print("\nLISTADO DE PEDIDOS")
    if len(pedidos) == 0:
        print("No hay pedidos")
    else:
        pos = 0
        for p in pedidos:
            total = 0
            for l in p["lineas"]:
                total = total + l["cantidad"] * l["precio"]
            if total > 100:
                total = total - total * 0.10
            elif total > 50:
                total = total - total * 0.05
            print(str(pos + 1) + ". Cliente: " + p["cliente"]["nombre"] + " | Estado: " + p["estado"] + " | Total: " + str(round(total, 2)) + " €")
            pos = pos + 1


def calcular_total_desde_menu():
    """Calcula y muestra el total detallado de un pedido específico.
    
    Solicita al usuario que seleccione un pedido por número,
    calcula el subtotal, aplica descuentos, calcula IVA (21%)
    y muestra el desglose completo del total.
    
    Returns:
        None
    
    Side Effects:
        Imprime el desglose de costos en la consola.
    """
    if len(pedidos) == 0:
        print("No hay pedidos")
        return

    n = pedir_numero("Número de pedido: ")
    if n < 1 or n > len(pedidos):
        print("Pedido no válido")
        return

    p = pedidos[n - 1]
    suma = 0
    for linea in p["lineas"]:
        suma = suma + linea["cantidad"] * linea["precio"]

    # Reglas de descuento duplicadas a propósito
    descuento = 0
    if suma > 100:
        descuento = suma * 0.10
    elif suma > 50:
        descuento = suma * 0.05

    iva = (suma - descuento) * 0.21
    total = suma - descuento + iva

    print("Subtotal: " + str(round(suma, 2)))
    print("Descuento: " + str(round(descuento, 2)))
    print("IVA: " + str(round(iva, 2)))
    print("TOTAL: " + str(round(total, 2)))


def cambiar_estado_pedido():
    """Cambia el estado de un pedido (función incompleta).
    
    Esta función es un marcador de código incompleto e intencional
    para detectar código muerto o funcionalidad no implementada.
    
    Returns:
        str: El nuevo estado ingresado por el usuario.
    
    Note:
        Esta función no está integrada en el menú principal
        y requiere completarse para ser funcional.
    
    Deprecated:
        Esta función está marcada para revisión y posible implementación.
    """
    x = input("Nuevo estado: ")
    return x
