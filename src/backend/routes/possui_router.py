from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.possui import PossuiSchema
from crud.possui import associar_pedido_usuario
from database import get_db

router = APIRouter()
    
@router.post("/associar/")
def pegar_pedidos_por_id(idusuario: int, codrastreio: str, db: Session = Depends(get_db)):
    return associar_pedido_usuario(db, PossuiSchema(idusuario=idusuario, codrastreio=codrastreio))
