from pydantic import BaseModel
from datetime import date
from typing import Optional

class PedidoSchema(BaseModel):
    codrastreio : str
    apelido : Optional[str]
    status : str
    transportadora : str
    dtultimoevento : Optional[date]
    local : str

    class Config:
        orm_mode = True