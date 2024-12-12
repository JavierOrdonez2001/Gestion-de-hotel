import mysql.connector

class LoginController:
    def __init__(self):
         self.config = {
            'user': 'root',
            'password': '1256347',
            'host': 'localhost',
            'database': 'hotel',
        }


    def login(self, email:str, password:str):
        try:
            # Conexión a la base de datos
            connection = mysql.connector.connect(**self.config)
            cursor = connection.cursor(dictionary=True)  # dictionary=True para obtener resultados como diccionarios

            # Consulta para validar el email y password y obtener el rol
            query = """
            SELECT u.id_user, u.name, u.email, u.password, r.role_name
            FROM users u
            INNER JOIN roles r ON u.role_id = r.id_role
            WHERE u.email = %s AND u.password = %s
            """
            cursor.execute(query, (email, password))
            result = cursor.fetchone()  # Obtener un único resultado

            # Si se encontró un usuario
            if result:
                # Crear el array de objetos con el usuario encontrado
                user_data = [{
                    "id_user": result["id_user"],
                    "name": result["name"],
                    "email": result["email"],
                    "role_name": result["role_name"]
                }]
                return True, user_data
            else:
                # Si no coincide
                return False, []

        except mysql.connector.Error as err:
            print(f"Error al validar el login: {err}")
            return False, []

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()