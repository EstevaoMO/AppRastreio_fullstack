from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.pedido import PedidoSchema
from crud.pedido import criar_pedido, pedidos_do_usuario, deletar_pedido
from database import get_db

router = APIRouter()
    
@router.get("/consultar_pedidos/{id}")
def pegar_pedidos_por_id(id: int, db: Session = Depends(get_db)):
    return pedidos_do_usuario(db, id)

@router.post("/adicionar", response_model=PedidoSchema)
def adicionar_pedido(pedido: PedidoSchema, db: Session = Depends(get_db)):
    return criar_pedido(db, pedido)

@router.post("/deletar")
def apagar_pedido(codigo: str, db: Session = Depends(get_db)):
    return deletar_pedido(db, codigo)
