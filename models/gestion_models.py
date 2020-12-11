from pydantic import BaseModel
from datetime import date

class GestionIn(BaseModel):
    docName: str
    expiration: date

class GestionOut(BaseModel):
    docName: str
    expiration: date
