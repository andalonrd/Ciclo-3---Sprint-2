from pydantic import BaseModel
from datetime import date
from datetime import datetime

class GestionIn(BaseModel):
    docName: str
    expiration: date

class GestionOut(BaseModel):
    id_gestion: int
    #date: datetime
    docName: str
    expiration: date