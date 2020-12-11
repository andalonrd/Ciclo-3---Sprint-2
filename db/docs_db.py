from typing import Dict
from pydantic import BaseModel
from datetime import date

class DocInDB(BaseModel):
    doc_Name: str
    field: str
    author: str
    expiration: date

database_docs = Dict[str, DocInDB]

database_docs = {
    "documento_medico": DocInDB(**{ "doc_Name": "documento_medico",
                                    "field": "medicina",
                                    "author": "Marisol",
                                    "expiration": "2019-12-15"}),
    "documento_legal": DocInDB(**{ "doc_Name": "documento_legal",
                                    "field": "legislación",
                                    "author": "Luis",
                                    "expiration": "2020-12-20"}),
    "documento_bancario": DocInDB(**{ "doc_Name": "documento_bancario",
                                    "field": "economia",
                                    "author": "Felipe",
                                    "expiration": "2021-6-17"})                              
}

def get_docs(doc_Name: str):
    if doc_Name in database_docs.keys():
        return database_docs[doc_Name]
    else:
        return None


def update_docs(doc_in_db: DocInDB):
    database_docs[doc_in_db.doc_Name] = doc_in_db
    return doc_in_db
