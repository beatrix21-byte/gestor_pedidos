import re


def validar_nombre(nombre):
    """Valida que el nombre no esté vacío ni sea solo espacios.
    
    Args:
        nombre (str): Nombre a validar.
    
    Returns:
        bool: True si el nombre es válido (no vacío y no solo espacios), False en caso contrario.
    
    Examples:
        >>> validar_nombre("Juan")
        True
        >>> validar_nombre("   ")
        False
        >>> validar_nombre("")
        False
    """
    return nombre and nombre.strip() != ""


def validar_email(email):
    """Valida que el email tenga un formato correcto.
    
    Verifica que el email cumpla con el patrón RFC básico:
    usuario@dominio.extensión
    
    Args:
        email (str): Dirección de email a validar.
    
    Returns:
        bool: True si el email tiene un formato válido, False en caso contrario.
    
    Examples:
        >>> validar_email("usuario@ejemplo.com")
        True
        >>> validar_email("correo-mal")
        False
    """
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(patron, email))


class Cliente:
    """Representa un cliente con validación de datos.
    
    Esta clase encapsula la información de un cliente y proporciona
    métodos para validar que los datos sean correctos.
    
    Attributes:
        nombre (str): Nombre completo del cliente.
        email (str): Dirección de correo electrónico del cliente.
        telefono (str, optional): Número de teléfono de contacto.
    """
    
    def __init__(self, nombre, email, telefono=None):
        """Inicializa una nueva instancia de Cliente.
        
        Args:
            nombre (str): Nombre completo del cliente.
            email (str): Dirección de correo electrónico del cliente.
            telefono (str, optional): Número de teléfono de contacto. Por defecto es None.
        
        Examples:
            >>> cliente = Cliente("Laura Pérez", "laura@example.com", "600111222")
            >>> cliente.nombre
            'Laura Pérez'
        """
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
    
    def es_valido(self):
        """Verifica si el cliente tiene datos válidos.
        
        Valida que el nombre no esté vacío y que el email tenga
        un formato correcto.
        
        Returns:
            bool: True si el cliente tiene datos válidos, False en caso contrario.
        
        Examples:
            >>> cliente = Cliente("Ana", "ana@example.com")
            >>> cliente.es_valido()
            True
            >>> cliente_invalido = Cliente(" ", "correo-mal")
            >>> cliente_invalido.es_valido()
            False
        """
        return validar_nombre(self.nombre) and validar_email(self.email)


clientes = []


def menu_clientes():
    """Muestra el menú interactivo de gestión de clientes.
    
    Presenta un menú con opciones para añadir, listar y buscar clientes.
    El menú se repite hasta que el usuario elige la opción de volver.
    
    Returns:
        None
    """
    terminar = False
    while not terminar:
        print("\n--- CLIENTES ---")
        print("1. Añadir cliente")
        print("2. Listar clientes")
        print("3. Buscar cliente")
        print("4. Volver")
        op = input("Opción: ")

        if op == "1":
            crear_cliente()
        elif op == "2":
            listar_clientes()
        elif op == "3":
            buscar_cliente()
        elif op == "4":
            terminar = True
        else:
            print("No existe esa opción")


def crear_cliente():
    """Crea un nuevo cliente interactivamente.
    
    Solicita al usuario que ingrese el nombre, teléfono y email
    de un nuevo cliente. Valida que el nombre no esté vacío
    antes de añadir el cliente a la lista.
    
    Returns:
        None
    
    Side Effects:
        Modifica la lista global 'clientes' añadiendo un nuevo cliente.
    """
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    email = input("Email: ")

    # Validación pobre a propósito para que se pueda mejorar
    if nombre == "":
        print("El nombre no puede estar vacío")
    else:
        cliente = {"nombre": nombre, "telefono": telefono, "email": email}
        clientes.append(cliente)
        print("Cliente añadido")


def listar_clientes():
    """Muestra todos los clientes registrados.
    
    Imprime en pantalla un listado numerado de todos los clientes
    con su nombre, teléfono y email. Si no hay clientes, muestra
    un mensaje informativo.
    
    Returns:
        None
    
    Side Effects:
        Imprime información en la consola.
    """
    print("\nLISTADO DE CLIENTES")
    if len(clientes) == 0:
        print("No hay clientes")
    else:
        i = 0
        while i < len(clientes):
            c = clientes[i]
            print(str(i + 1) + ". " + c["nombre"] + " - " + c["telefono"] + " - " + c["email"])
            i = i + 1


def buscar_cliente():
    """Busca clientes por nombre, teléfono o email.
    
    Solicita al usuario un texto de búsqueda y busca coincidencias
    parciales (case-insensitive para nombre y email) en los datos
    de los clientes registrados. Imprime los resultados encontrados.
    
    Returns:
        None
    
    Side Effects:
        Imprime los clientes encontrados o mensaje de no encontrados.
    """
    texto = input("Texto a buscar: ")
    encontrado = False
    for c in clientes:
        if texto.lower() in c["nombre"].lower() or texto in c["telefono"] or texto.lower() in c["email"].lower():
            print(c["nombre"] + " - " + c["telefono"] + " - " + c["email"])
            encontrado = True
    if not encontrado:
        print("No se encontraron clientes")
