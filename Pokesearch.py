import sys
import requests
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QVBoxLayout, QWidget, QDialog
from PySide6.QtGui import QPixmap, QColor, QPalette
from PySide6.QtGui import QMovie
from PySide6.QtCore import QSize, QRect

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Pokédex")
        # self.setGeometryBasedOnScreen()
        self.setFixedSize(650, 850)

        self.setStyleSheet("""
            QPushButton {
                background-color: dark-grey;
                color: white;
                border: 1px solid #FC7300;
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
                background-color: #FC953F;
                color: dark-grey;
            }
        """)

        labelmov = QLabel(self)
        labelmov.setScaledContents(True)
        movie = QMovie("poke.gif.gif")
        labelmov.setGeometry(QRect(0, 0, 1200, 800))
        labelmov.setMovie(movie)
        movie.start() 

        pushButton = QPushButton(parent=self, text='Ready')
        pushButton.setGeometry(50, 300, 160, 43)
        pushButton.clicked.connect(self.fetch_pokemon_info)

        self.labelpic = QLabel(self)
        self.labelpic.setGeometry(QRect(400, 20, 550, 700))
        self.labelpic.setPixmap(QPixmap(""))
        self.labelpic.setScaledContents(True)

        self.show()

    # def setGeometryBasedOnScreen(self):
    #     screen = QApplication.primaryScreen()
    #     if screen is not None:
    #         available_geometry = screen.availableGeometry()
    #         width, height = available_geometry.width(), available_geometry.height()
    #         window_width = int(width * 0.3)
    #         window_height = int(height * 0.6)
    #         x = int((width - window_width) / 2)
    #         y = int((height - window_height) / 2)
    #         self.setGeometry(x, y, window_width, window_height)

    def fetch_pokemon_info(self):
        pokemon_name = self.pokemon_name_input.text()

        
        pokemon_data = {
            "name": "Pikachu",
            "type": "Electric",
            "height": "0.4 m",
            "weight": "6.0 kg",
            # Add more attributes as needed
        }

        self.display_pokemon_info(pokemon_data)

    def display_pokemon_info(self, pokemon_data):
        self.w = QDialog(self)
        self.w.setWindowTitle("Pokédex - Pokémon Information")
        self.w.setGeometry(400, 200, 300, 200)

        layout = QVBoxLayout()
        for key, value in pokemon_data.items():
            label = QLabel(f"{key}: {value}")
            layout.addWidget(label)

        layout.addWidget(QLabel("Enter Pokémon Name:"))
        self.pokemon_name_input = QLineEdit()
        layout.addWidget(self.pokemon_name_input)

        pushButton = QPushButton(text='Fetch')
        pushButton.clicked.connect(self.fetch_pokemon_info)
        layout.addWidget(pushButton)

        self.w.setLayout(layout)
        self.w.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
