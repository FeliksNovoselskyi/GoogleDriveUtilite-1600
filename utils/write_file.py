

# Додаткова утиліта для збереження завантаженного файлу в download_file.py
def write_file(file_name, data):
    with open(f"media/{file_name}", "wb") as file:
        file.write(data)

