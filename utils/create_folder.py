from config import service_drive


def create_folder(name,parent):

    service_drive.files().create(
        body = {
            "name": name,
            "mimeType": "application/vnd.google-apps.folder",
            "parents": [parent]
        }
    ).execute()
