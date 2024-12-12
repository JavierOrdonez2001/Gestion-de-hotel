import mysql.connector
from uuid import uuid4

class AdminController:
    def __init__(self):
        self.config = {
            'user': 'root',
            'password': '1256347',
            'host': 'localhost',
            'database': 'hotel',
        }

    def get_id_role_by_name(self, role_name: str) :
        try:
            connection = mysql.connector.connect(**self.config)
            cursor = connection.cursor()
            query = "SELECT id_role, role_name FROM roles WHERE role_name = %s"
            cursor.execute(query, (role_name,))
            role = cursor.fetchone()
            role_arr = [{"id_role": role[0], "role_name": role[1]}]
            return role_arr[0]['id_role']
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def create_user_encargado(self,name, email, password, role_id):
        try:
            id_user = str(uuid4())
        
            connection = mysql.connector.connect(**self.config)
            cursor = connection.cursor()
            query = "INSERT INTO users (id_user, name, email, password, role_id) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query,(id_user, name, email, password, role_id))
            connection.commit()
            return "Usuario creado con exito"
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
        
        