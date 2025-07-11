from sqlalchemy.orm import Session
from models.possui import PossuiModel
from schemas.possui import PossuiSchema

def associar_pedido_usuario(db: Session, associacao: PossuiSchema):
    nova_associacao = PossuiModel(idusuario=associacao.idusuario, codrastreio=associacao.codrastreio)
    db.add(nova_associacao)
    db.commit()
    db.refresh(nova_associacao)
    
    return nova_associacao