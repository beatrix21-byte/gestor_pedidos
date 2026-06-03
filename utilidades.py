def mostrar_titulo(t):
    print("\n============================")
    print(t)
    print("============================")


def pedir_numero(mensaje):
    valor = input(mensaje)
    try:
        return int(valor)
    except ValueError:
        print("Número no válido. Se usará 0")
        return 0


def formatear_moneda(x):
    return str(round(x, 2)) + " €"
