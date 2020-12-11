<<<<<<< HEAD
from pydantic import BaseModel
from datetime import datetime

class DocIn(BaseModel):
    docName: str

class DocOut(BaseModel):
    id_gestion: int
    docName: str
    date: datetime
    expiration: datetime
=======
from pydantic import BaseModel
from datetime import datetime

class GestionIn(BaseModel):
    docName: str

class GestionOut(BaseModel):
    id_gestion: int
    docName: str
    date: datetime
    expiration: datetime
>>>>>>> 79c12619e5f8addf8a92fe35b5d6cfbdafe429a1
