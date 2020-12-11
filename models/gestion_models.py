from pydantic import BaseModel
from datetime import datetime

class AccessIn(BaseModel):
  doc_name: str
  
class AccessOut(BaseModel):
  id_access: int
  doc_name: str
  date: datetime
  end_date: datetime
