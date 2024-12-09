from db.db_factory import Base
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship

class Room(Base):
    
    __tablename__ = 'rooms'

    id_room = Column(String(50), primary_key=True)
    room_number = Column(String(30), nullable=False, unique=True)
    number_people = Column(Integer, nullable=False)
    orientation = Column(String(100), nullable=False)
    active = Column(Boolean, default=False)

    client_assignment_id = Column(String(50),  ForeignKey('client_assignment.id_assignment'))


    client_assignment = relationship('Client_assignment', back_populates='room')