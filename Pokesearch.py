import sys
import requests
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QVBoxLayout, QWidget, QDialog
from PySide6.QtGui import QPixmap, QColor, QPalette
from PySide6.QtGui import QMovie
from PySide6.QtCore import QSize, QRect
from SearchWindow import SearchWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.w = None

    def initUI(self):
        self.setWindowTitle("Pokédex")
        # self.setGeometryBasedOnScreen()
        self.setFixedSize(850, 478)

        self.setStyleSheet("""
            QPushButton {
                background-color: dark-grey;
                color: white;
                border: 1px solid #BA263E;
                font: bold 16px;
                text-align: center;
                border-radius: 10px;
            }
            QMainWindow {
                background-color: #B1322F;
            }
            QLabel {
                font-size: 18px;
            }
            QPushButton:hover {
                background-color: #BA263E;
                color: dark-grey;
            }
        """)
        # place an image.png
        self.label = QLabel(self)
        self.label.setGeometry(QRect(0, 0, 850,478))
        self.label.setPixmap(QPixmap("landing.jpg"))
        self.label.setScaledContents(True)

       



        pushButton = QPushButton(parent=self, text='GO!')
        pushButton.setGeometry(50, 300, 160, 43)
        pushButton.clicked.connect(self.open_search_window)
    
        self.labelpic = QLabel(self)
        self.labelpic.setGeometry(QRect(400, 20, 550, 700))
        self.labelpic.setPixmap(QPixmap(""))
        self.labelpic.setScaledContents(True)

        self.show()
    def open_search_window(self, checked):
        if self.w is None:
            self.w = SearchWindow()
        self.w.show()
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
