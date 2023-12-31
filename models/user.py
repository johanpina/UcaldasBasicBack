from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100))
    email = Column(String(100), unique=True)
    password = Column(String(100))
    rol_id = Column(Integer, ForeignKey("roles.id"))

    rol = relationship("Rol", back_populates="users")


class Rol(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100))

    users = relationship("User", back_populates="rol")