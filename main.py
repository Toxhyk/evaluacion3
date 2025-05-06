from auth import login
from models import inicializar_datos
from vendedor import realizar_pedido
from admin import ver_reportes, editar_stock
from utils import clear_screen

def main():
    inicializar_datos()
    while True:
        clear_screen()
        print("--- Sistema de Pedidos Acme Smoked Fish ---")
        user = login()
        if not user:
            input("Presione ENTER para intentar nuevamente...")
            continue

        while True:
            print("\n--- Menú ---")
            print("1. Realizar pedido")
            if user["role"] == "admin":
                print("2. Ver reportes")
                print("3. Editar stock")
            print("0. Cerrar sesión")

            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                realizar_pedido(user)
            elif opcion == "2" and user["role"] == "admin":
                ver_reportes()
            elif opcion == "3" and user["role"] == "admin":
                editar_stock()
            elif opcion == "0":
                break
            else:
                print("Opción inválida.")

            input("\nPresione ENTER para continuar...")

if __name__ == "__main__":
    main()
