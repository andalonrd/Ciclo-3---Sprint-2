from pydantic import BaseModel
from datetime import datetime

class GestionIn(BaseModel):
    docName: str

class GestionOut(BaseModel):
    id_gestion: int
    docName: str
    date: datetime
    expiration: datetime
