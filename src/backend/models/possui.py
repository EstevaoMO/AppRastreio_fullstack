from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class PossuiModel(Base):
    __tablename__ = "possui"

    idusuario = Column(Integer, ForeignKey("usuario.idusuario", ondelete="CASCADE"), primary_key=True)
    codrastreio = Column(String(200), ForeignKey("pedido.codrastreio", ondelete="CASCADE"), primary_key=True)

    usuario = relationship("usuario", back_populates="pedido")
    pedido = relationship("pedido", back_populates="usuario")