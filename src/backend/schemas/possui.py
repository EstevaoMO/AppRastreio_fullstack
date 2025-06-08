from pydantic import BaseModel

class PossuiSchema(BaseModel):
    idusuario : int
    codrastreio : str