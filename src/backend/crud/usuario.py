from sqlalchemy.orm import Session
from models.usuario import UsuarioModel
from schemas.usuario import UsuarioCriarSchema

def criar_usuario(db: Session, usuario: UsuarioCriarSchema):
    usuario_criado = UsuarioModel(nomeusuario=usuario.nomeusuario)
    db.add(usuario_criado)
    db.commit()
    db.refresh(usuario_criado)
    
    return usuario_criado

def usuario_por_id(db: Session, id: int):
    return db.query(UsuarioModel).filter(UsuarioModel.idusuario == id).first()

def deletar_usuario(db: Session, id: int):
    usuario = db.query(UsuarioModel).filter(UsuarioModel.idusuario == id).first()
    
    if usuario:
        db.delete(usuario)
        db.commit()
    
    return usuario