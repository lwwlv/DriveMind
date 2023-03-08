import sys

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QWidget, QApplication

def Entry():
    App = QApplication(sys.argv)

    Window = QWidget()
    Window.resize(800, 600)
    Window.setWindowTitle('DriveMind')
    Window.show()

    sys.exit(App.exec())

if __name__ == '__main__':
    Entry()