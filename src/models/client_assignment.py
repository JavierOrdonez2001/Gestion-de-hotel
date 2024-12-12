from db.db_factory import Base
from sqlalchemy import Column, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship

from src.models.room import Room

class Client_assignment(Base):

    __tablename__ = 'client_assignment'
    
    id_assignment = Column(String(50), primary_key=True)
    date = Column(Date, nullable=False)
    client_name = Column(String(100), nullable=False)
    client_rut = Column(String(30), nullable=False, unique=True)
    client_number = Column(Float, nullable=False)
    room_number = Column(String(20), nullable=False)

    id_usuario = Column(String(50), ForeignKey('users.id_user', ondelete='SET NULL'), nullable=True)
    user = relationship('User', back_populates='client_assignment')

    room = relationship(Room, back_populates='client_assignment')