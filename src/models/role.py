from db.db_factory import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Role(Base):
    __tablename__ = 'roles'

    id_role = Column(String(50), primary_key=True)
    role_name = Column(String(50), nullable=False, unique=True)

    user = relationship('User', back_populates='role')


