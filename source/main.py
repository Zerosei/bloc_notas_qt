import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QDialog, QPushButton, QLabel, QApplication
from PyQt5.QtCore import *
from ui_nueva_nota import Ui_Dialog  # Interfaz ventana nueva
from ui_mainwindow import Ui_MainWindow  # Importo la interfaz principal
import os


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Inicializamos la interfaz (esto es lo generado por pyuic5)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  # Configura la interfaz en la ventana principal

        self.ui.pushButton.clicked.connect(lambda: self.new_txt())
        self.ui.verticalLayout.setDirection(QVBoxLayout.BottomToTop)
        self.ui.label.setText("")
        self.ui.verticalLayout_2.setDirection(QVBoxLayout.BottomToTop)
        self.ui.deleteButton.hide()
        self.ui.editButton.hide()


    def new_txt(self):
        dialog = QDialog()
        dialog_ui = Ui_Dialog()
        dialog_ui.setupUi(dialog)
        dialog_ui.save_button.clicked.connect(lambda: self.create_txt(dialog_ui, dialog))
        dialog.exec_()


    def create_txt(self, dialog_ui, dialog, edit=False, txt=None):
        i=0

        content_text = dialog_ui.content.toPlainText()

        if not edit:
            header_text_temp = dialog_ui.header.toPlainText().replace("txt", "")
            header_text = header_text_temp.replace("\t", "")
            txt_files = [file for file in os.listdir(os.getcwd()) if file.endswith(".txt")]
            while f"{header_text}.txt" in txt_files:
                header_text += f"({i})"
            with open(f'{header_text}.txt', 'w') as file:
                file.write(content_text)
            dialog.accept()
            self.add_to_list_of_txts(f"{header_text}.txt")
        else:
            with open(txt, 'w') as file:
                file.write(content_text)
            dialog.accept()
            self.open_txt(txt)
            self.ui.editButton.clicked.disconnect()







    def get_number_of_txts(self):
        txt_files = [file for file in os.listdir(os.getcwd()) if file.endswith(".txt")]
        for file in txt_files:
            button = QPushButton()
            if len(file) > 22:
                button.setText(file[:22] + "...")
            else:
                button.setText(file)

            button.setObjectName(file)

            button.clicked.connect(lambda _, f=file: self.open_txt(f))

            button.setStyleSheet(
            """
            QPushButton { 
            border: 0.5px solid lightgrey; 
            border-radius: 10px; 
            background-color: #F5F5F5; 
            color: #2D336B ;
            }
            
            QPushButton::hover {
            background-color: #A9B5DF; }
            """)

            button.setFixedSize(190, 60)
            self.ui.verticalLayout.addWidget(button)


    def add_to_list_of_txts(self, txt):
        button = QPushButton()
        button.setObjectName(txt)
        if len(txt) > 22:
            button.setText(txt[:22] + "...")
        else:
            button.setText(txt)

        button.clicked.connect(lambda _, f=txt: self.open_txt(f))

        button.setStyleSheet(
            """
            QPushButton { 
            border: 0.5px solid lightgrey; 
            border-radius: 10px; 
            background-color: #F5F5F5; 
            color: #2D336B ;
            }

            QPushButton::hover {
            background-color: #A9B5DF; }
            """)

        button.setFixedSize(190, 50)
        self.ui.verticalLayout.addWidget(button)


    def open_txt(self, txt_name):
        self.ui.deleteButton.show()
        self.ui.editButton.show()

        if self.ui.verticalLayout_2.count() == 2:
            last_item = self.ui.verticalLayout_2.itemAt(self.ui.verticalLayout_2.count() - 1)
            if last_item.widget():
                last_item.widget().deleteLater()
        with open(txt_name, 'r') as file:
            text = file.read()

        self.ui.content_header.setText(" " + txt_name[:40])
        self.ui.content_header.setWordWrap(True)

        try:
            self.ui.editButton.clicked.disconnect()
        except  TypeError:
            pass

        label = QLabel(text)
        label.setWordWrap(True)
        label.setObjectName("Contenido")
        label.setFont(QFont('Arial', 14))
        label.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        self.ui.verticalLayout_2.addWidget(label)
        self.ui.deleteButton.clicked.connect(lambda: self.delete_txt(txt_name))
        self.ui.editButton.clicked.connect(lambda: self.edit_txt(txt_name))

    def delete_txt(self, txt_name):
        os.remove(txt_name)
        for widget in self.ui.scrollArea.findChildren(QPushButton):
            if widget.objectName() == txt_name:
                self.ui.verticalLayout.removeWidget(widget)
                widget.deleteLater()

        self.ui.deleteButton.clicked.disconnect()
        self.ui.deleteButton.hide()
        self.ui.editButton.clicked.disconnect()
        self.ui.editButton.hide()
        self.ui.content_header.setText("")

        for widget in self.ui.si.findChildren(QLabel):
            if widget.objectName() == "Contenido":
                widget.deleteLater()

    def edit_txt(self, txt_name):
        text_to_edit = ""
        for widget in self.ui.si.findChildren(QLabel):
            if widget.objectName() == "Contenido":
                text_to_edit = widget.text()
        dialog = QDialog()
        dialog_ui = Ui_Dialog()
        dialog.setWindowTitle("Editar nota")
        dialog_ui.setupUi(dialog)
        dialog_ui.header.setText(txt_name)
        dialog_ui.header.setDisabled(True)
        dialog_ui.content.setText(text_to_edit)
        dialog_ui.save_button.clicked.connect(lambda: self.create_txt(dialog_ui, dialog, True, txt_name))
        dialog.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    window.get_number_of_txts()
    sys.exit(app.exec_())

