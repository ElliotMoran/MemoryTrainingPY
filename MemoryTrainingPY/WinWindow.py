from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow


class WinWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('resources/ui/winWindow.ui', self)
        self.setFixedSize(740, 360)
        self.move(10, 10)

        self.game = None
        self.exitButton.clicked.connect(self.exit)

    def addGame(self, game):
        self.game = game

    def exit(self):
        self.close()
        self.game.exit()
