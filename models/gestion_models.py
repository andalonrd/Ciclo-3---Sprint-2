from pydantic import BaseModel
from datetime import datetime

class GestionIn(BaseModel):
  doc_name: str
  
class GestionOut(BaseModel):
  id_access: int
  doc_name: str
  date: datetime
  expiration: datetime
