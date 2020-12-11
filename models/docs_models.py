from pydantic import BaseModel
from datetime import datetime

class DocIn(BaseModel):
    docName: str

class DocOut(BaseModel):
    id_gestion: int
    docName: str
    date: datetime
    expiration: datetime