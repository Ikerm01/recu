def mostrar_menu():
    print("Bienvenido a la Pizzería")
    print("1. Tomar pedido")
    print("2. Quieres editar el pedido?")
    print("3. Cobrar pedido")
    print("4. Salir")

def tomar_pedido():
    print("Tomando pedido...")

def editar_pedido():
    print("Preparando pedido...")

def cobrar_pedido():
    print("Cobrando pedido...")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            tomar_pedido()
        elif opcion == '2':
            tomar_pedido()
        elif opcion == '3':
            cobrar_pedido()
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")
        
