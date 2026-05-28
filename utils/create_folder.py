from googleapiclient.errors import HttpError

from config import service_drive


def create_folder(folder_name, parent_folder_id):
    try:
        service_drive.files().create(
            body = {
                "name": folder_name,
                "mimeType": "application/vnd.google-apps.folder",
                "parents": [parent_folder_id]
            }
        ).execute()
    
    except HttpError as error:
        print(error)
