<<<<<<< HEAD
from pydantic import BaseModel
from datetime import datetime

class GestionIn(BaseModel):
    docName: str
    field: str
    author: str

class GestionOut(BaseModel):
    docName: str
    expiration: datetime
=======
from datetime import datetime
from pydantic import BaseModel

class GestionInDB(BaseModel):
  id_gestion: int = 0
  doc_Name: str
  date: datetime = datetime.now()
  expiration: datetime

database_gestion = []
generator = {"id":0}
  
  
def save_gestion(gestion_in_db: GestionInDB):
  generator["id"] = generator["id"] + 1
  gestion_in_db.id_gestion = generator["id"]
  database_gestion.append(gestion_in_db)
  return gestion_in_db
>>>>>>> 79c12619e5f8addf8a92fe35b5d6cfbdafe429a1
