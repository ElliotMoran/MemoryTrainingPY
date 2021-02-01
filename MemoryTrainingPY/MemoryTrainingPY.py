import sys
import sqlite3
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QObject

from Autorization import Autorization
from WinWindow import WinWindow
from MainMenu import MainMenu
from Game import Game


class MemoryTraining(QObject):
    def __init__(self):
        super().__init__()
        self.mainMenu = MainMenu()
        self.mainMenu.show()
        self.mainMenu.setEnabled(False)

        self.winWindow = WinWindow()

        self.game = Game()
        self.game.addMenu(self.mainMenu)

        self.game.addWinWindow(self.winWindow)
        self.winWindow.addGame(self.game)
        self.mainMenu.addGame(self.game)

        self.autorization = Autorization()
        self.autorization.addMenu(self.mainMenu)
        self.autorization.show()
        self.mainMenu.addAuto(self.autorization)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MemoryTraining()
    sys.exit(app.exec_())
