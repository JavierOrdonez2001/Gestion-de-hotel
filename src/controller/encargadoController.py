import mysql.connector
from uuid import uuid4
import datetime

class EncargadoController:
    def __init__(self):
        self.config = {
            'user': 'root',
            'password': '1256347',
            'host': 'localhost',
            'database': 'hotel',
        }

    
    def register_room(self, room_number:str, number_people:int, orientation:str, active:bool, price:float):

        try:
            
            id_room = str(uuid4())

            
            connection = mysql.connector.connect(**self.config)
            cursor = connection.cursor()

            
            query = """
            INSERT INTO rooms (id_room, room_number, number_people, orientation, active, client_assignment_id, price)
            VALUES (%s, %s, %s, %s, %s, NULL, %s)
            """
            values = (id_room, room_number, number_people, orientation, active, price)

          
            cursor.execute(query, values)
            connection.commit()

            print(f"Habitación registrada con éxito. ID: {id_room}")
            return id_room

        except mysql.connector.Error as err:
            print(f"Error al registrar la habitación: {err}")
            return None

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()


    def client_assignment(self, room_number, email, client_name, client_rut, client_number ):
        try:
            client_number_int = int(client_number)
            id_assignment_uuid = uuid4()
            id_assignment = str(id_assignment_uuid)
            
            today = datetime.date.today()
            connection = mysql.connector.connect(**self.config)
            cursor = connection.cursor()
            query1 = """
            SELECT active, id_room, number_people 
            FROM rooms
            WHERE rooms.room_number = %s;
            """
            cursor.execute(query1, (room_number,))
            result = cursor.fetchone()
            
            connection.commit()
            if result == None:
                return f'La habitacion con el numero {room_number} no existe'
            if result[0] == 1:
                return f'La habitacion con el numero {room_number} no esta disponible'
            number_people = result[2]
            if client_number_int > number_people:
                return f'La habitacion solo tiene la capacidad de {number_people} personas'
            if client_number_int <= 0:
                return f'El numero de clientes para ser asignados es invalida'
            id_room = result[1]
            
            
            

            query2 = """
            SELECT id_user 
            FROM users
            WHERE email = %s;
            """

            cursor.execute(query2, (email,))
            user_result = cursor.fetchone()
            id_user = user_result[0]

            query3 = """
            INSERT INTO client_assignment (id_assignment, date, client_name, client_rut, client_number, id_usuario, room_number)
            VALUES (%s, %s, %s, %s, %s, %s, %s);
            """
            values = (id_assignment, today, client_name, client_rut, client_number_int, id_user, room_number)

            cursor.execute(query3, values)
            connection.commit()

            query4 = """
            UPDATE rooms
            SET active = 1
            WHERE room_number = %s;
            """
            cursor.execute(query4, (room_number,))
            connection.commit()

            return f'Esignacion exitosa para el cliente {client_name}'
            


            
        




        
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()


    def get_client_assignment(self):
        try:
            # Conectar a la base de datos
            connection = mysql.connector.connect(**self.config)
            cursor = connection.cursor(dictionary=True)

            # Consulta para obtener el nombre del cliente y número de la habitación
            query = """
            SELECT client_name, room_number
            FROM client_assignment;
            """
            cursor.execute(query)

            # Obtener los resultados
            results = cursor.fetchall()

            # Convertir resultados en una lista de objetos
            client_assignments = [{"client_name": row["client_name"], "room_number": row["room_number"]} for row in results]

            # Imprimir la tabla para visualización (opcional)
            print("Tabla de asignaciones:")
            for assignment in client_assignments:
                print(f"Cliente: {assignment['client_name']}, Habitación: {assignment['room_number']}")

            return client_assignments

        except mysql.connector.Error as err:
            print(f"Error al obtener las asignaciones: {err}")
            return []

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()  


    def get_rooms_actived(self):
        try:
            # Conectar a la base de datos
            connection = mysql.connector.connect(**self.config)
            cursor = connection.cursor(dictionary=True)

            # Consulta para obtener habitaciones activas
            query = """
            SELECT id_room, room_number, number_people, orientation, price
            FROM rooms
            WHERE active = 1;
            """
            cursor.execute(query)

            # Obtener los resultados
            results = cursor.fetchall()

            # Convertir resultados en una lista de objetos
            rooms_actived = [
                {
                    "id_room": row["id_room"],
                    "room_number": row["room_number"],
                    "number_people": row["number_people"],
                    "orientation": row["orientation"],
                    "price": row["price"],
                }
                for row in results
            ]

            # Imprimir habitaciones activas (opcional)
            print("Habitaciones activas:")
            for room in rooms_actived:
                print(f"Habitación: {room['room_number']}, Capacidad: {room['number_people']}, Orientación: {room['orientation']}, Precio: {room['price']}")

            return rooms_actived

        except mysql.connector.Error as err:
            print(f"Error al obtener habitaciones activas: {err}")
            return []

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def get_rooms_inactived(self):
        try:
            # Conectar a la base de datos
            connection = mysql.connector.connect(**self.config)
            cursor = connection.cursor(dictionary=True)

            # Consulta para obtener habitaciones inactivas
            query = """
            SELECT id_room, room_number, number_people, orientation, price
            FROM rooms
            WHERE active = 0;
            """
            cursor.execute(query)

            # Obtener los resultados
            results = cursor.fetchall()

            # Convertir resultados en una lista de objetos
            rooms_inactived = [
                {
                    "id_room": row["id_room"],
                    "room_number": row["room_number"],
                    "number_people": row["number_people"],
                    "orientation": row["orientation"],
                    "price": row["price"],
                }
                for row in results
            ]

            # Imprimir habitaciones inactivas (opcional)
            print("Habitaciones inactivas:")
            for room in rooms_inactived:
                print(f"Habitación: {room['room_number']}, Capacidad: {room['number_people']}, Orientación: {room['orientation']}, Precio: {room['price']}")

            return rooms_inactived

        except mysql.connector.Error as err:
            print(f"Error al obtener habitaciones inactivas: {err}")
            return []

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()