from pydantic import BaseModel
from datetime import date

class DocIn(BaseModel):
    docName: str

class DocOut(BaseModel):
    docName: str
    field: str
    author: str
    expiration: date