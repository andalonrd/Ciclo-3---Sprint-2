from db.docs_db import DocInDB
from db.docs_db import get_docs, update_docs
from models.docs_models import DocIn, DocOut

from db.gestion_db import GestionInDB
from db.gestion_db import save_gestion
from models.gestion_models import GestionIn, GestionOut

import datetime
from fastapi import FastAPI
from fastapi import HTTPException

api = FastAPI()

@api.post("/user/auth/")
async def auth_user(doc_in: DocIn):
    today = date.today()
    docs_in_db = get_docs(docs_in.docName)
    if docs_in_db == None:
        raise HTTPException(status_code=404,
            detail="El documento no existe")
    if docs_in_db.expiration < today:
        return {"Caducado": False}
    return {"Caducado": True}

@api.get("/docs/balance/{docName}")
async def get_document(docName: str):
    docs_in_db = get_docs(docName)
    if docs_in_db == None:
        raise HTTPException(status_code=404,
                            detail="El documento no existe")
    docs_out = DocOut(**docs_in_db.dict())
    return docs_out


@api.put("/docs/update/")
async def make_operation(gestion_in: GestionIn):
    today = date.today()
    docs_in_db = get_docs(gestion_in.docName)
    if docs_in_db == None:
        raise HTTPException(status_code=404,
                            detail="Documento no existe")
    if docs_in_db.expiration <= today:
        raise HTTPException(status_code=400,
                            detail="Documento caducado")
    else:
        print("Documento esta vigente")

    gestion_in_db = GestionInDB(**gestion_in.dict())
    gestion_in_db = save_gestion(gestion_in_db)

    gestion_out = GestionOut(**gestion_in_db.dict())
    return gestion_out