from db.db_factory import Base
from sqlalchemy import Column, String, Date

class Record(Base):
    
    __tablename__ = 'records'


    id_record = Column(String(50), primary_key=True)
    date = Column(Date, nullable=False)
    id_user = Column(String(50))
    email_user = Column(String(50), unique=True)
    name_client = Column(String(50))
    rut_client = Column(String(30), unique=True)
    room_number = Column(String(30), unique=True)
