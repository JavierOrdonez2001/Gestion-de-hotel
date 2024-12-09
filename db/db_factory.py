from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker , declarative_base

Base = declarative_base()



class Db_factory:

    @staticmethod
    def get_engine(username:str, password:str, host:str, port:int, database:str):
        connection_string = f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
        return create_engine(connection_string, echo=True)
    
    @staticmethod
    def get_session(engine):
        return sessionmaker(bind=engine)
    

