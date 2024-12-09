from db.db_factory import Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'

    id_user = Column(String(50), primary_key=True)
    name = Column(String(50),nullable=False,)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(30), nullable=False)

    role_id = Column(String(50), ForeignKey('roles.id_role'))
    role = relationship('Role', back_populates='user')

    client_assignment = relationship('Client_assignment', back_populates='user')

    