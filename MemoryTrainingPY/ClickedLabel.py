from PyQt5.QtWidgets import QLabel
from PyQt5.Qt import pyqtSignal


class ClickedLabel(QLabel):
    def __init__(self):
        super().__init__()
        self.name = ""
        self.wasClicked = False
        self.outOfGame = False

    clicked = pyqtSignal()

    def mouseReleaseEvent(self, e):
        super().mouseReleaseEvent(e)
        self.clicked.emit()

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name
