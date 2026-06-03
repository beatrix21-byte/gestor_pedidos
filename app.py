from pedidos import menu_pedidos
from clientes import menu_clientes
from utilidades import mostrar_titulo


def main():
    salir = False
    while salir == False:
        mostrar_titulo("GESTOR DE PEDIDOS")
        print("1. Clientes")
        print("2. Pedidos")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            menu_clientes()
        elif opcion == "2":
            menu_pedidos()
        elif opcion == "3":
            print("Hasta pronto")
            salir = True
        else:
            print("Opción incorrecta")


main()
