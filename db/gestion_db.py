from datetime import date
from datetime import datetime
from pydantic import BaseModel

class GestionInDB(BaseModel):
    expiration: date
    id_gestion: int = 0
    registro: datetime 
    doc_Name: str    

database_gestion = []
generator = {"id":0}
  
  
def save_gestion(gestion_in_db: GestionInDB):
  generator["id"] = generator["id"] + 1
  gestion_in_db.id_gestion = generator["id"]
  database_gestion.append(gestion_in_db)
  return gestion_in_db