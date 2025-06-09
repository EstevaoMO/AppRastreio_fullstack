from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.usuario import UsuarioCriarSchema
from crud.usuario import usuario_por_id, criar_usuario, deletar_usuario
from database import get_db

router = APIRouter()
    
@router.get("/{id}")
def pegar_usuario_por_id(id: int, db: Session = Depends(get_db)):
    return usuario_por_id(db, id)

@router.post("/cadastrar", response_model=UsuarioCriarSchema)
def cadastrar_usuario(usuario: UsuarioCriarSchema, db: Session = Depends(get_db)):
    return criar_usuario(db, usuario)

@router.post("/deletar")
def apagar_usuario(id: int, db: Session = Depends(get_db)):
    return deletar_usuario(db, id)
