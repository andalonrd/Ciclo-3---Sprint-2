from pydantic import BaseModel
from datetime import date
from datetime import datetime

class GestionIn(BaseModel):
    doc_Name: str
    expiration: date

class GestionOut(BaseModel):
    id_gestion: int
    registro: datetime 
    doc_Name: str
    expiration: date