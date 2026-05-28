from googleapiclient.http import MediaFileUpload

from config import service_drive


def upload_file(file_name, folder_id, mime_type):
    
    try:
        # Вказуємо метадані створюваного файлу на диску
        file_metadata = {
            "name": file_name,
            "parents": [folder_id]
        }
        
        # Створюємо тіло з даними файлу
        media_body = MediaFileUpload(
            filename = f"media/{file_name}", # Шлях до локального файлу, звідки будуть отримані його дані (у байтах)
            mimetype = mime_type # Вказуємо тип локального файлу, тобто тип, під яким він збережений на компʼютері
        )
        
        # Створюємо файл на диску, вказавши його основні дані та метадані
        service_drive.files().create(
            body = file_metadata,
            media_body = media_body
        ).execute()
        
    except Exception as error:
        print(error)

