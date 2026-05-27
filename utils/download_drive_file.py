# Импортировать сервисы
from config import service_drive
import io
from googleapiclient.http import MediaIoBaseDownload

# Написать утилиту для загрузки файла с диска
def download_drive_file(file_id, file_name, file_type):
    if file_type == "googlefile":
        data = service_drive.files().export(
            fileId = file_id,
            mimeType = file_type
        ).execute()
        
    else:
        request = service_drive.files().get_media(fileId = file_id)
        
        data = io.BytesIO()
        
        downloader = MediaIoBaseDownload(data, request)
        done = False
        
        while done is False:
            status, done = downloader.next_chunk()
            print(f"Download {int(status.progress() * 100)}.")
        
        data.seek(0)
    
    with open(f"media/{file_name}", "wb") as file:
        file.write(data.read())

# if type == "googlefile":

# "mediafile"