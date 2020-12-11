from datetime import datetime
from pydantic import BaseModel

class AccessInDB(BaseModel):
  id_access: int = 0
  username: str
  date: datetime = datetime.now()
  value: int

 database_access = []
 generator = {"id":0}
  
  
def save_access(access_in_db: AccessInDB):
  generator["id"] = generator["id"] + 1
  access_in_db.id_access = generator["id"]
  database_access.append(access_in_db)
  return access_in_db
