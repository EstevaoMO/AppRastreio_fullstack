from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class UsuarioModel(Base):
    __tablename__ = "usuario"

    idusuario = Column(Integer, primary_key=True, autoincrement=True)
    nomeusuario = Column(String(100), nullable=False)

    possuis = relationship("PossuiModel", back_populates="usuario", cascade="all, delete")
