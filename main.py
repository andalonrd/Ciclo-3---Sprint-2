from db.docs_db import DocInDB
from db.docs_db import get_docs, update_docs
from models.doc_models import DocIn, DocOut

from db.gestion_db import GestionInDB
from db.gestion_db import save_gestion


import datetime
from fastapi import FastAPI
from fastapi import HTTPException
api = FastAPI()


@api.get("/docs/balance/{docName}")
async def get_document(docName: str):
    docs_in_db = get_docs(docName)
    if docs_in_db == None:
        raise HTTPException(status_code=404,
                            detail="El documento no existe")
    docs_out = DocOut(**docs_in_db.dict())
    return docs_out


@api.put("/docs/update/")
async def make_operation(transaction_in: TransactionIn):
    today = date.today()
    docs_in_db = get_docs(transaction_in.username)
    if docs_in_db == None:
        raise HTTPException(status_code=404,
                            detail="Documento no existe")
    if docs_in_db.expiration < today:
        raise HTTPException(status_code=400,
                            detail="Documento caducado")
    else:
        print("Documento esta vigente")

docs_in_db.balance = docs_in_db.balance - gestion_in.value
update_docs(docs_in_db)

gestion_in_db = GestionInDB(**gestion_in.dict(),
    actual_balance = docs_in_db.balance)
gestion_in_db = save_gestion(gestion_in_db)

gestion_out = GestionOut(**gestion_in_db.dict())
return gestion_out
