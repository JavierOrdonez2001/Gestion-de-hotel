from db.db_factory import Db_factory, Base
from src.models.client_assignment import Client_assignment
from src.models.record import Record
from src.models.role import Role
from src.models.room import Room
from src.models.user import User

print('Rellena los campos para la conexion y creacion de tablas.\n')




username = input('username: ') 
password = input('password: ') 
host = input('host: ') 
port_input = input('port: ') 
port = int(port_input) or 3306
database = input('data base: ') 

engine = Db_factory.get_engine(username,password,host,port,database) 



print("Creando tablas...")
Base.metadata.create_all(engine)
print(Base.metadata.tables.keys())
print("Tablas creadas correctamente.")