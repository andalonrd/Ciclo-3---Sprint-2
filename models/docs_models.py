from pydantic import BaseModel
from datetime import date

class DocIn(BaseModel):
    docName: str

class DocOut(BaseModel):
    docName: str
    field: str
    author: str
<<<<<<< HEAD
    expiration: date
=======
    expiration: date
>>>>>>> 080ebe17fa91accb9705f921f249d5e67de5ccca
