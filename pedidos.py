from clientes import clientes
from utilidades import pedir_numero

pedidos = []


def menu_pedidos():
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
    # Función sin usar, pensada para detectar código muerto o incompleto
    x = input("Nuevo estado: ")
    return x
