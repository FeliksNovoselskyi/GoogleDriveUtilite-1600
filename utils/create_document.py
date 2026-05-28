from googleapiclient.errors import HttpError

from config import service_docs, service_drive


def create_document(title, content, folder_id):
    
    # Роботу з API вказуємо у блоці try, 
    # для можливості обробки помилок під час надсилання запиту
    try:
        # Створюємо документ (зберігається на диску користувача, що запустив застосунок)
        document = service_docs.documents().create(
            body = {
                "title": f"{title}"
            }
        ).execute()
        
        document_id = document["documentId"]
        
        # Вказуємо контент документа
        service_docs.documents().batchUpdate(
            documentId = document_id,
            body = {
                "requests": [
                    {
                        "insertText": {
                            "text": content,
                            "location": {"index": 1},
                        }
                    }
                ]
            }
        ).execute()
        
        # Переміщуємо документ до вказаної папки на диску
        service_drive.files().update(
            fileId = document["documentId"],
            addParents = folder_id
        ).execute()
        
    except HttpError as error:
        print(error)

