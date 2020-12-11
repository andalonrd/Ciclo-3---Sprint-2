
def document_log(i,user,doc_name,log):
    if user != "" :
        from datetime import date 
        i += 1
        registry = {"id": i , "date": str(date.today()), "user": user, "doc_name": doc_name }
        log.append(registry)
    return i    
     
def document_metadata(inList,doc_name):
    for x in inList: 
        if x['doc_name'] == doc_name :
            return x 

db = [{"doc_name": "hello.doc", "user": "kitty25", "expiry": "2020-12-30"},
 {"doc_name": "sunshine.doc", "user": "mags25", "expiry": "2020-12-25"}, 
  {"doc_name": "bridge.doc", "user": "cutie24", "expiry": "2021-1-25"}, 
  { "doc_name": "ice.doc", "user": "pinky27", "expiry": "2021-1-06" }
 ]  

doc_i = 0
doc_log = []
found_doc = document_metadata(db,"sunshine.doc")
print (found_doc)
doc_i = document_log(doc_i, found_doc['user'], found_doc['doc_name'],doc_log)
found_doc = document_metadata(db,"bridge.doc")
print(found_doc)
doc_i = document_log(doc_i, found_doc['user'], found_doc['doc_name'],doc_log)
print(doc_log)

