from pydantic import BaseModel

class UsuarioCriarSchema(BaseModel):
    nomeusuario : str

class UsuarioConsultarSchema(BaseModel):
    idusuario : int

    class Config:
        orm_mode = True