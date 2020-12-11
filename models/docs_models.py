from pydantic import BaseModel

class DocIn(BaseModel):
    docName: str
    field: str
    author: str

class DocOut(BaseModel):
    docName: str
    expiration: date
