from pydantic import BaseModel

class UsuarioCriarSchema(BaseModel):
    nome : str

class UsuarioConsultarSchema(BaseModel):
    id : int

    class Config:
        orm_mode = True