from sqlalchemy import Column, Date, String
from sqlalchemy.orm import relationship
from database import Base

class PedidoModel(Base):
    __tablename__ = "pedido"

    codrastreio = Column(String(200), primary_key=True, nullable=False)
    apelido = Column(String(100), nullable=True)
    status = Column(String(50), nullable=True)
    local = Column(String(100), nullable=True)
    dtultimoevento = Column(Date, nullable=True)
    transportadora = Column(String(50), nullable=True)

    possuis = relationship("PossuiModel", back_populates="pedido", cascade="all, delete")