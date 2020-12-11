from db.docs_db import DocInDB
from db.docs_db import get_docs, update_docs
from models.docs_models import DocIn, DocOut

from db.gestion_db import GestionInDB
from db.gestion_db import save_gestion
from models.gestion_models import GestionIn, GestionOut

from datetime import date
from fastapi import FastAPI
from fastapi import HTTPException

api = FastAPI()

@api.post("/docs/verify/")
async def auth_user(doc_in: DocIn):
    today = date.today()
    doc_in_db = get_docs(doc_in.docName)
    if doc_in_db == None:
        raise HTTPException(status_code=404,
            detail="El documento no existe")
    if doc_in_db.expiration < today:
        return {"El documento continúa vigente": False}
    return {"El documento continúa vigente": True}

@api.get("/docs/balance/{docName}")
async def get_document(docName: str):
    doc_in_db = get_docs(docName)
    if doc_in_db == None:
        raise HTTPException(status_code=404,
                            detail="El documento no existe")
    docs_out = DocOut(**doc_in_db.dict())
    return docs_out

@api.put("/docs/update/")
async def make_operation(gestion_in: GestionIn):
    today = date.today()
    doc_in_db = get_docs(gestion_in.docName)
    if doc_in_db == None:
        raise HTTPException(status_code=404,
                            detail="Documento no existe")
    if doc_in_db.expiration < today:
        raise HTTPException(status_code=400,
                            detail="Documento caducado")
    else:
        print("Documento esta vigente")

    doc_in_db.expiration = gestion_in.expiration
    
    update_docs(doc_in_db)
    gestion_in_db = GestionInDB(**gestion_in.dict(),expiration = doc_in_db.expiration)
    gestion_in_db = save_gestion(gestion_in_db)

    gestion_out = GestionOut(**gestion_in_db.dict())
    return gestion_out