import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtGui import QScreen
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Poke-Search")
        self.setGeometryBasedOnScreen()
        self.setStyleSheet("background-colour: red")
        self.show()

    def setGeometryBasedOnScreen(self):
        screen = QApplication.primaryScreen()
        if screen is not None:
            available_geometry = screen.availableGeometry()
            width, height = available_geometry.width(), available_geometry.height()
            window_width = int(width * 0.3)
            window_height = int(height * 0.6)
            x = int((width - window_width) / 2)
            y = int((height - window_height) / 2)

            self.setGeometry(x, y, window_width, window_height)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())