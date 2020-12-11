from pydantic import BaseModel
from datetime import datetime

class GestionIn(BaseModel):
    docName: str
    field: str
    author: str

class GestionOut(BaseModel):
    docName: str
    expiration: datetime
