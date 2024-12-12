from src.controller.adminController import AdminController
from src.controller.loginController import LoginController
from src.controller.encargadoController import EncargadoController

def main():
    admin_controller = AdminController()
    login_controller = LoginController()
    encargado_controller = EncargadoController()

    print("--- Sistema de Gestión de Habitaciones ---")
    
    # Inicio de sesión
    email = input("Ingresa tu correo electrónico: ")
    password = input("Ingresa tu contraseña: ")

    logged_in, user_data = login_controller.login(email, password)

    if not logged_in:
        print("Credenciales incorrectas. Por favor, inténtalo de nuevo.")
        return

    role_name = user_data[0]["role_name"]
    print(f"Bienvenido, {user_data[0]['name']}! Tu rol es: {role_name}")

    if role_name == "Administrador":
        while True:
            print("\n--- Menú Administrador ---")
            print("1. Crear usuario encargado")
            print("2. Salir")

            choice = input("Selecciona una opción: ")

            if choice == "1":
                # Crear usuario encargado
                name = input("Nombre del encargado: ")
                email = input("Correo del encargado: ")
                password = input("Contraseña del encargado: ")
                role_id = admin_controller.get_id_role_by_name("Encargado")
                result = admin_controller.create_user_encargado(name, email, password, role_id)
                print(result)

            elif choice == "2":
                print("Cerrando sesión...")
                break

            else:
                print("Opción inválida. Por favor, selecciona una opción válida.")

    elif role_name == "Encargado":
        while True:
            print("\n--- Menú Encargado ---")
            print("1. Registrar habitación")
            print("2. Asignar cliente a habitación")
            print("3. Ver asignaciones de clientes")
            print("4. Ver habitaciones activas")
            print("5. Ver habitaciones inactivas")
            print("6. Salir")

            choice = input("Selecciona una opción: ")

            if choice == "1":
                # Registrar habitación
                room_number = input("Número de la habitación: ")
                number_people = int(input("Capacidad de personas: "))
                orientation = input("Orientación de la habitación: ")
                active = bool(int(input("¿Está activa? (1 para Sí, 0 para No): ")))
                price = float(input("Precio de la habitación: "))
                encargado_controller.register_room(room_number, number_people, orientation, active, price)

            elif choice == "2":
                # Asignar cliente a habitación
                room_number = input("Número de la habitación: ")
                email = input("Correo del usuario responsable: ")
                client_name = input("Nombre del cliente: ")
                client_rut = input("RUT del cliente: ")
                client_number = int(input("Número de personas asignadas: "))
                result = encargado_controller.client_assignment(room_number, email, client_name, client_rut, client_number)
                print(result)

            elif choice == "3":
                # Ver asignaciones de clientes
                assignments = encargado_controller.get_client_assignment()
                print("Asignaciones de clientes:")
                for assignment in assignments:
                    print(f"Cliente: {assignment['client_name']}, Habitación: {assignment['room_number']}")

            elif choice == "4":
                # Ver habitaciones activas
                active_rooms = encargado_controller.get_rooms_actived()
                print("Habitaciones activas:")
                for room in active_rooms:
                    print(f"Habitación: {room['room_number']}, Capacidad: {room['number_people']}, Orientación: {room['orientation']}, Precio: {room['price']}")

            elif choice == "5":
                # Ver habitaciones inactivas
                inactive_rooms = encargado_controller.get_rooms_inactived()
                print("Habitaciones inactivas:")
                for room in inactive_rooms:
                    print(f"Habitación: {room['room_number']}, Capacidad: {room['number_people']}, Orientación: {room['orientation']}, Precio: {room['price']}")

            elif choice == "6":
                print("Cerrando sesión...")
                break

            else:
                print("Opción inválida. Por favor, selecciona una opción válida.")
    else:
        print("Rol no reconocido. Por favor, contacta al administrador.")

if __name__ == "__main__":
    main()
