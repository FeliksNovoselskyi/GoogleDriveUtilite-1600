import io
from googleapiclient.http import MediaIoBaseDownload, HttpError

from config import service_drive

from .write_file import write_file


def download_file(file_id, file_name, file_type, export_mime_type):
    try:
        if file_type == "googlefile":
            data = service_drive.files().export(
                fileId = file_id,
                mimeType = export_mime_type
            ).execute()
            
            write_file(
                file_name = file_name,
                data = data
            )
            
        elif file_type == "mediafile":
            request = service_drive.files().get_media(
                fileId = file_id
            )
            
            data = io.BytesIO()
            
            downloader = MediaIoBaseDownload(data, request)
            done = False
            
            while done is False:
                status, done = downloader.next_chunk()
                print(f"Download {int(status.progress() * 100)}.")
            
            data.seek(0)
            
            write_file(
                file_name = file_name,
                data = data.read()
            )
        
    except HttpError as error:
        print(error)
