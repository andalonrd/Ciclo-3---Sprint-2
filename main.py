from db.docs_db import DocInDB
from db.docs_db import get_docs, update_docs
from models.doc_models import DocIn, DocOut




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
