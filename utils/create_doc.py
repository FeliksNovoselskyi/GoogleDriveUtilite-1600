from config import service_docs


def create_doc(file_name):
    
    service_docs.documents().create(
        body = {"title" : f"{file_name}"}
    ).execute()
    
    # batchUpdate
    
    # update

list1 = []
list1.index()