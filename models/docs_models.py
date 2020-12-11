from pydantic import BaseModel
from datetime import date

class DocIn(BaseModel):
    doc_Name: str

class DocOut(BaseModel):
    doc_Name: str
    field: str
    author: str
    expiration: date