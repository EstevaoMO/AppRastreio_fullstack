from sqlalchemy.orm import Session
from models.pedido import PedidoModel
from models.possui import PossuiModel
from schemas.pedido import PedidoSchema
from schemas.possui import PossuiSchema

def criar_pedido(db: Session, pedido: PedidoSchema):
    pedido_criado = PedidoModel(
            codrastreio=pedido.codrastreio,
            apelido=pedido.apelido,
            status=pedido.status,
            transportadora=pedido.transportadora,
            dtultimoevento=pedido.dtultimoevento,
            local=pedido.local
        )
    
    db.add(pedido_criado)
    db.commit()
    db.refresh(pedido_criado)
    
    return pedido_criado

def pedidos_do_usuario(db: Session, id: int):
    return db.query(PedidoModel).join(PossuiModel).filter(PossuiModel.idusuario == id).all()

def deletar_pedido(db: Session, codrastreio: str):
    pedido = db.query(PedidoModel).filter(PedidoModel.codrastreio == codrastreio).first()
    
    if pedido:
        db.delete(pedido)
        db.commit()
    
    return pedido