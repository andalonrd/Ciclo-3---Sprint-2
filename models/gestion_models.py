from pydantic import BaseModel
from datetime import date
from datetime import datetime

class GestionIn(BaseModel):
    docName: str
    expiration: date

class GestionOut(BaseModel):
    id_gestion: int
    registro: datetime
    docName: str
<<<<<<< HEAD
    expiration: date
=======
    expiration: date
>>>>>>> 080ebe17fa91accb9705f921f249d5e67de5ccca
