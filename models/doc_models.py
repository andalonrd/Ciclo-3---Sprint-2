from pydantic import BaseModel

class DocIn(BaseModel):
    docName: str
    field: str

class DocOut(BaseModel):
    docName: str
    field: str
    author: str
    expiration: date