from typing import Dict
from pydantic import BaseModel
from datetime import date

class DocInDB(BaseModel):
    docName: str
    field: str
    author: str
    expiration: date

database_docs = Dict[str, DocInDB]

database_docs = {
    "documento_medico": DocInDB(**{ "docName": "documento_medico",
                                    "field": "medicina",
                                    "author": "Marisol",
                                    "expiration": (2020-12-15)}),
    "documento_legal": DocInDB(**{ "docName": "documento_legal",
                                    "field": "legislación",
                                    "author": "Luis",
                                    "expiration": (2020-12-20)}),
    "documento_bancario": DocInDB(**{ "docName": "documento_bancario",
                                    "field": "economia",
                                    "author": "Felipe",
                                    "expiration": (2021-6-17)})                              
}

def get_docs(docName: str):
    if docName in database_docs.keys():
        return database_docs[docName]
    else:
        return None


def update_docs(doc_in_db: DocInDB):
    database_docs[doc_in_db.docName] = doc_in_db
    return doc_in_db
<<<<<<< HEAD


=======
>>>>>>> 79c12619e5f8addf8a92fe35b5d6cfbdafe429a1
