from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class PossuiModel(Base):
    __tablename__ = "possui"

    idusuario = Column(Integer, ForeignKey("usuario.idusuario", ondelete="CASCADE"), primary_key=True)
    codrastreio = Column(String(200), ForeignKey("pedido.codrastreio", ondelete="CASCADE"), primary_key=True)

    usuario = relationship("UsuarioModel", back_populates="possuis")
    pedido = relationship("PedidoModel", back_populates="possuis")