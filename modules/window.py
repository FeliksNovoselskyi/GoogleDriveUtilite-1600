
import PyQt6.QtWidgets as widgets
import PyQt6.QtCore as core
import PyQt6.QtGui as gui

# Назар. Импортировать утилиты
from utils import create_doc, create_folder, download_drive_file, download_file_on_drive 


class MainWindow(widgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(100, 100, 720, 1024)
        
        central_widget = widgets.QWidget(self)
        central_widget.setFixedSize(1024, 720)
        central_widget_layout = widgets.QVBoxLayout()
        central_widget_layout.setAlignment(core.Qt.AlignmentFlag.AlignLeft)
        central_widget.setLayout(central_widget_layout)
        
        
        # Створення документу
        title_label = widgets.QLabel("Створення документу", parent=central_widget)
        central_widget_layout.addWidget(title_label)

        self.DOC_NAME = widgets.QLineEdit(parent = central_widget)
        self.DOC_NAME.setPlaceholderText("Введіть назву документу")
        self.DOC_NAME.setFixedWidth(600)
        central_widget_layout.addWidget(self.DOC_NAME)
        
        self.DOC_CONTENT = widgets.QTextEdit(parent=central_widget)
        self.DOC_CONTENT.setPlaceholderText("Введіть текст документу")
        self.DOC_CONTENT.setFixedWidth(600)
        central_widget_layout.addWidget(self.DOC_CONTENT)
        # Создать поле для id папки
        self.ID = widgets.QLineEdit(parent=central_widget)
        self.ID.setFixedWidth(600)
        self.ID.setPlaceholderText("Введіть ID папки")
        central_widget_layout.addWidget(self.ID)
        # Создать кнопку "Створити"
        create_button = widgets.QPushButton(parent=central_widget, text="Створити")
        create_button.setFixedWidth(600)
        create_button.clicked.connect(self.create_document)        
        central_widget_layout.addWidget(create_button)
        
        
        
        # Створення папки
        self.LABEL_TITLE = widgets.QLabel(parent=central_widget, text="Створення папки")
        central_widget_layout.addWidget(self.LABEL_TITLE)
        
        # Создать поле ввода для названия папки
        self.LABEL_INPUT = widgets.QLineEdit(parent=central_widget)
        self.LABEL_INPUT.setPlaceholderText("Назва папки")
        self.LABEL_INPUT.setFixedWidth(600)
        
        central_widget_layout.addWidget(self.LABEL_INPUT)
        # Создать поле ввода для id родительской папки
        self.INPUT_PARENT_ID = widgets.QLineEdit(parent=central_widget)
        self.INPUT_PARENT_ID.setPlaceholderText("ID батьківської папки")
        self.INPUT_PARENT_ID.setFixedWidth(600)

        central_widget_layout.addWidget(self.INPUT_PARENT_ID)
        # Создать кнопку
        self.BUTTON_CREATE = widgets.QPushButton(parent=central_widget, text="Створити")
        self.BUTTON_CREATE.setFixedWidth(600)
        self.BUTTON_CREATE.clicked.connect(self.create_folder)
        central_widget_layout.addWidget(self.BUTTON_CREATE)

        # Завантажити файл з диску
        self.DOWNLOAD_LABEL = widgets.QLabel(text = "Завантажити файл з диску", parent = central_widget)
        
        self.ID_LINE_EDIT = widgets.QLineEdit(parent = central_widget)
        self.ID_LINE_EDIT.setPlaceholderText("Id файлу")
        self.ID_LINE_EDIT.setFixedWidth(600)
        
        self.FILE_NAME_LINE_EDIT = widgets.QLineEdit(parent = central_widget)
        self.FILE_NAME_LINE_EDIT.setPlaceholderText("Назва файлу")
        self.FILE_NAME_LINE_EDIT.setFixedWidth(600)
        
        self.FILE_TYPE_LINE_EDIT = widgets.QLineEdit(parent = central_widget)
        self.FILE_TYPE_LINE_EDIT.setPlaceholderText("Тип файлу (googlefile або mediafile)")
        self.FILE_TYPE_LINE_EDIT.setFixedWidth(600)
        
        self.DOWNLOAD_BUTTON = widgets.QPushButton(text = "Завантажити", parent = central_widget)
        self.DOWNLOAD_BUTTON.setStyleSheet("background-color: grey; color: white;")
        self.DOWNLOAD_BUTTON.clicked.connect(self.button_signal)
        self.DOWNLOAD_BUTTON.setFixedWidth(600)
        
        central_widget_layout.addWidget(self.DOWNLOAD_LABEL)
        central_widget_layout.addWidget(self.ID_LINE_EDIT)
        central_widget_layout.addWidget(self.FILE_NAME_LINE_EDIT)
        central_widget_layout.addWidget(self.FILE_TYPE_LINE_EDIT)
        central_widget_layout.addWidget(self.DOWNLOAD_BUTTON)
        
        # Завантажити файл на диск
        self.DOWNLOAD_FILE_LABEL = widgets.QLabel(text = "Завантажити файл на диск", parent = central_widget)
        
        self.FILE_NAME = widgets.QLineEdit(parent = central_widget)
        self.FILE_NAME.setPlaceholderText("Назва файлу")
        self.FILE_NAME.setFixedWidth(600)
        
        self.FOLDER_ID = widgets.QLineEdit(parent = central_widget)
        self.FOLDER_ID.setPlaceholderText("Id папки")
        self.FOLDER_ID.setFixedWidth(600)
        
        self.MIME_TYPE = widgets.QLineEdit(parent = central_widget)
        self.MIME_TYPE.setPlaceholderText("MimeType файлу")
        self.MIME_TYPE.setFixedWidth(600)
        
        self.DOWNLOAD_FILE_BUTTON = widgets.QPushButton(text = "Завантажити", parent = central_widget)
        self.DOWNLOAD_FILE_BUTTON.setStyleSheet("background-color: grey; color: white;")
        self.DOWNLOAD_FILE_BUTTON.setFixedWidth(600)
        self.DOWNLOAD_FILE_BUTTON.clicked.connect(self.download_file_on_disk)

        central_widget_layout.addWidget(self.DOWNLOAD_FILE_LABEL)
        central_widget_layout.addWidget(self.FILE_NAME)
        central_widget_layout.addWidget(self.FOLDER_ID)
        central_widget_layout.addWidget(self.MIME_TYPE)
        central_widget_layout.addWidget(self.DOWNLOAD_FILE_BUTTON)

    
    def create_document(self):
        doc_name = self.DOC_NAME.text()
        doc_content = self.DOC_CONTENT.toPlainText()
        id = self.ID.text() 
        
        create_doc(file_name = doc_name )
        
        print(doc_name, doc_content, id)
    
    def create_folder(self):
        folder_name = self.LABEL_INPUT.text()
        parent_id = self.INPUT_PARENT_ID.text()
        
        create_folder(name= folder_name, parent=parent_id)
        
        print(folder_name, parent_id)
    
    def button_signal(self):
        
        id = self.ID_LINE_EDIT.text()
        name = self.FILE_NAME_LINE_EDIT.text()
        type = self.FILE_TYPE_LINE_EDIT.text()
        
        download_drive_file(file_id= id, file_name=name, file_type=type)

        print(id, name, type)
    
    def download_file_on_disk(self):
        file_name = self.FILE_NAME.text()
        folder_id = self.FOLDER_ID.text()
        mime_type = self.MIME_TYPE.text()
        
        download_file_on_drive()

        print(file_name, folder_id, mime_type)

window = MainWindow()

