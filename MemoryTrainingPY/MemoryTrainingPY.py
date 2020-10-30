import sys

from PIL import Image
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.Qt import pyqtSignal
import random


class ClickedLabel(QLabel):
    def __init__(self):
        super().__init__()
        self.name = ""
        self.wasClicked = False

    clicked = pyqtSignal()

    def mouseReleaseEvent(self, e):
        super().mouseReleaseEvent(e)
        self.clicked.emit()

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name


class Autorization(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('authorization.ui', self)
        self.mainMenu = None
        self.bd = dict()
        self.check = False

        self.registerButton.clicked.connect(self.register)
        self.loginButton.clicked.connect(self.login)

    def addBd(self, bd):
        self.bd = bd

    def getBd(sefl):
        return self.bd

    def register(self):
        name = self.nickEdit.text()
        password = self.passEdit.text()
        if (name in self.bd.keys()):
            if (len(name) < 4 and len(password) < 4):
                self.warningLabel.setText("Short Nickname or password")
            else:
                self.warningLabel.setText("Username is taken!")
        else:
            if (len(name) < 4 and len(password) < 4):
                self.warningLabel.setText("Short Nickname or password")
            else:
                self.bd[name] = password
                self.mainMenu.setEnabled(True)
                self.close()
                return True

    def login(self):
        name = self.nickEdit.text()
        password = self.passEdit.text()
        if (name in self.bd.keys() and len(name) > 3):
            if (self.bd[name] != password and len(password) < 4):
                self.warningLabel.setText("Wrong Password!")
            else:
                self.chek = True
                self.mainMenu.setEnabled(True)
                self.close()
        else:
            self.warningLabel.setText("Wrong Nickname!")


    def checkAutorization(self):
        return self.check

    def addMenu(self, menu):
        self.mainMenu = menu


class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('mainMenu.ui', self)
        
        self.game = None

        self.startButton.clicked.connect(self.startGame)
        self.exitButton.clicked.connect(self.exit)

    def exit(self):
        sys.exit()

    def startGame(self):
        self.close()
        self.game.show()

    def addGame(self, game):
        self.game = game

class Game(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("game.ui", self)
        self.setupUi()

        self.pics = ["pics/auto1.jpg", "pics/auto2.jpg", "pics/auto3.jpg", "pics/auto4.jpg",
                     "pics/auto5.jpg", "pics/auto6.jpg", "pics/auto7.jpg", "pics/auto8.jpg",
                     "pics/auto1.jpg", "pics/auto2.jpg", "pics/auto3.jpg", "pics/auto4.jpg",
                     "pics/auto5.jpg", "pics/auto6.jpg", "pics/auto7.jpg", "pics/auto8.jpg"]

        self.labels = [self.picPart_1, self.picPart_2, self.picPart_3, self.picPart_4,
                       self.picPart_5, self.picPart_6, self.picPart_7, self.picPart_8,
                       self.picPart_9, self.picPart_10, self.picPart_11, self.picPart_12,
                       self.picPart_13, self.picPart_14, self.picPart_15, self.picPart_16]


        self.errors = 0
        self.mainMenu = None
        self.firstTime = True

        self.startButton.clicked.connect(self.start)
        self.stopButton.clicked.connect(self.stop)
        self.exitButton.clicked.connect(self.exit)
        
        self.sec = 0
        self.timer = QTimer()
        self.set_time()
        self.timer.timeout.connect(self.counter)

        self.random_pic()
        self.makeAllDefault()
        

        self.picPart_1.clicked.connect(self.picClicked)
        self.picPart_2.clicked.connect(self.picClicked)
        self.picPart_3.clicked.connect(self.picClicked)
        self.picPart_4.clicked.connect(self.picClicked)
        self.picPart_5.clicked.connect(self.picClicked)
        self.picPart_6.clicked.connect(self.picClicked)
        self.picPart_7.clicked.connect(self.picClicked)
        self.picPart_8.clicked.connect(self.picClicked)
        self.picPart_9.clicked.connect(self.picClicked)
        self.picPart_10.clicked.connect(self.picClicked)
        self.picPart_11.clicked.connect(self.picClicked)
        self.picPart_12.clicked.connect(self.picClicked)
        self.picPart_13.clicked.connect(self.picClicked)
        self.picPart_14.clicked.connect(self.picClicked)
        self.picPart_15.clicked.connect(self.picClicked)
        self.picPart_16.clicked.connect(self.picClicked)

    def setupUi(self):
        self.picPart_3 = ClickedLabel()
        self.picPart_3.setObjectName("picPart_3")
        self.gridLayout.addWidget(self.picPart_3, 0, 2, 1, 1)
        self.picPart_2 = ClickedLabel()
        self.picPart_2.setObjectName("picPart_2")
        self.gridLayout.addWidget(self.picPart_2, 0, 1, 1, 1)
        self.picPart_5 = ClickedLabel()
        self.picPart_5.setObjectName("picPart_5")
        self.gridLayout.addWidget(self.picPart_5, 1, 0, 1, 1)
        self.picPart_4 = ClickedLabel()
        self.picPart_4.setObjectName("picPart_4")
        self.gridLayout.addWidget(self.picPart_4, 0, 3, 1, 1)
        self.picPart_15 = ClickedLabel()
        self.picPart_15.setObjectName("picPart_15")
        self.gridLayout.addWidget(self.picPart_15, 3, 2, 1, 1)
        self.picPart_16 = ClickedLabel()
        self.picPart_16.setObjectName("picPart_16")
        self.gridLayout.addWidget(self.picPart_16, 3, 3, 1, 1)
        self.picPart_14 = ClickedLabel()
        self.picPart_14.setObjectName("picPart_14")
        self.gridLayout.addWidget(self.picPart_14, 3, 1, 1, 1)
        self.picPart_13 = ClickedLabel()
        self.picPart_13.setObjectName("picPart_13")
        self.gridLayout.addWidget(self.picPart_13, 3, 0, 1, 1)
        self.picPart_1 = ClickedLabel()
        self.picPart_1.setObjectName("picPart_1")
        self.gridLayout.addWidget(self.picPart_1, 0, 0, 1, 1)
        self.picPart_12 = ClickedLabel()
        self.picPart_12.setObjectName("picPart_12")
        self.gridLayout.addWidget(self.picPart_12, 2, 3, 1, 1)
        self.picPart_9 = ClickedLabel()
        self.picPart_9.setObjectName("picPart_9")
        self.gridLayout.addWidget(self.picPart_9, 2, 0, 1, 1)
        self.picPart_8 = ClickedLabel()
        self.picPart_8.setObjectName("picPart_8")
        self.gridLayout.addWidget(self.picPart_8, 1, 3, 1, 1)
        self.picPart_11 = ClickedLabel()
        self.picPart_11.setObjectName("picPart_11")
        self.gridLayout.addWidget(self.picPart_11, 2, 2, 1, 1)
        self.picPart_6 = ClickedLabel()
        self.picPart_6.setObjectName("picPart_6")
        self.gridLayout.addWidget(self.picPart_6, 1, 1, 1, 1)
        self.picPart_7 = ClickedLabel()
        self.picPart_7.setObjectName("picPart_7")
        self.gridLayout.addWidget(self.picPart_7, 1, 2, 1, 1)
        self.picPart_10 = ClickedLabel()
        self.picPart_10.setObjectName("picPart_10")
        self.gridLayout.addWidget(self.picPart_10, 2, 1, 1, 1)

        self.picPart_1.setName("1")
        self.picPart_2.setName("2")
        self.picPart_3.setName("3")
        self.picPart_4.setName("4")
        self.picPart_5.setName("5")
        self.picPart_6.setName("6")
        self.picPart_7.setName("7")
        self.picPart_8.setName("8")
        self.picPart_9.setName("9")
        self.picPart_10.setName("10")
        self.picPart_11.setName("11")
        self.picPart_12.setName("12")
        self.picPart_13.setName("13")
        self.picPart_14.setName("14")
        self.picPart_15.setName("15")
        self.picPart_16.setName("16")

        self.makeAllOff()
        

    def random_pic(self):
        random.shuffle(self.pics)

    def makeAllOn(self):
        self.picPart_1.setEnabled(True)
        self.picPart_2.setEnabled(True)
        self.picPart_3.setEnabled(True)
        self.picPart_4.setEnabled(True)
        self.picPart_5.setEnabled(True)
        self.picPart_6.setEnabled(True)
        self.picPart_7.setEnabled(True)
        self.picPart_8.setEnabled(True)
        self.picPart_9.setEnabled(True)
        self.picPart_10.setEnabled(True)
        self.picPart_11.setEnabled(True)
        self.picPart_12.setEnabled(True)
        self.picPart_13.setEnabled(True)
        self.picPart_14.setEnabled(True)
        self.picPart_15.setEnabled(True)
        self.picPart_16.setEnabled(True)

    def makeAllOff(self):
        self.picPart_1.setEnabled(False)
        self.picPart_2.setEnabled(False)
        self.picPart_3.setEnabled(False)
        self.picPart_4.setEnabled(False)
        self.picPart_5.setEnabled(False)
        self.picPart_6.setEnabled(False)
        self.picPart_7.setEnabled(False)
        self.picPart_8.setEnabled(False)
        self.picPart_9.setEnabled(False)
        self.picPart_10.setEnabled(False)
        self.picPart_11.setEnabled(False)
        self.picPart_12.setEnabled(False)
        self.picPart_13.setEnabled(False)
        self.picPart_14.setEnabled(False)
        self.picPart_15.setEnabled(False)
        self.picPart_16.setEnabled(False)


    def makeAllDefault(self):
        self.picPart_1.setPixmap(QPixmap("pics/default.jpg"))
        self.picPart_2.setPixmap(QPixmap("pics/default.jpg"))
        self.picPart_3.setPixmap(QPixmap("pics/default.jpg"))
        self.picPart_4.setPixmap(QPixmap("pics/default.jpg"))
        self.picPart_5.setPixmap(QPixmap("pics/default.jpg"))
        self.picPart_6.setPixmap(QPixmap("pics/default.jpg"))
        self.picPart_7.setPixmap(QPixmap("pics/default.jpg"))
        self.picPart_8.setPixmap(QPixmap("pics/default.jpg"))
        self.picPart_9.setPixmap(QPixmap("pics/default.jpg"))
        self.picPart_10.setPixmap(QPixmap("pics/default.jpg"))
        self.picPart_11.setPixmap(QPixmap("pics/default.jpg"))
        self.picPart_12.setPixmap(QPixmap("pics/default.jpg"))
        self.picPart_13.setPixmap(QPixmap("pics/default.jpg"))
        self.picPart_14.setPixmap(QPixmap("pics/default.jpg"))
        self.picPart_15.setPixmap(QPixmap("pics/default.jpg"))
        self.picPart_16.setPixmap(QPixmap("pics/default.jpg"))

    def showAll(self):
        for el in self.labels:
            el.setPixmap(QPixmap(self.pics[int(el.getName()) - 1]))

    def picClicked(self):
        # не работает
        sender = self.sender()
        if (sender.wasClicked):
            return
        sender.wasClicked = True
        sender.setPixmap(QPixmap(self.pics[int(sender.getName()) - 1]))
        for el in self.labels:
            def make2Default():
                sender.setPixmap(QPixmap("pics/default.jpg"))
                el.setPixmap(QPixmap("pics/default.jpg"))
                print("ok")

            if el == sender:
                continue
            if el.wasClicked:
                if self.pics[int(el.getName()) - 1] == self.pics[int(sender.getName()) - 1]:
                    self.timerScreen = QTimer()
                    self.timerScreen.setSingleShot(True)
                    self.timerScreen.timeout.connect(make2Default)
                    self.timerScreen.start(1000)
                    sender.setEnabled(False)
                    el.setEnabled(False)
                else:

                    self.errors += 1
                    self.wrongsNumber.display(self.errors)
                    self.timerScreen = QTimer()
                    self.timerScreen.setSingleShot(True)
                    self.timerScreen.timeout.connect(make2Default)
                    self.timerScreen.start(1000)
                    sender.wasClicked = False
                    el.wasClicked = False
                    
    def checkAll(self):
        for el in self.label:
            if not el.isEnabled():
                return False
        return True

    def start(self):
        if self.firstTime:
            self.timerScreen = QTimer()
            self.timerScreen.setSingleShot(True)
            self.timerScreen.timeout.connect(self.makeAllDefault)
            self.timerScreen.start(1999)
            self.timerScreen1 = QTimer()
            self.timerScreen1.setSingleShot(True)
            self.timerScreen1.timeout.connect(self.makeAllOn)
            self.timerScreen1.start(2000)
            self.showAll()
        self.timer.start(1000)
        self.wrongsNumber.display(self.errors)

    def stop(self):
        self.timer.stop()
        self.firstTime = False
        self.makeAllDefault()
        self.makeAllOff()
        self.errors = 0

    def counter(self):
        self.sec += 1
        self.set_time()

    def is_timer_active(self):
        return self.timer.isActive()

    def set_time(self):
        hour = self.sec / 3600
        minut = (self.sec % 3600) / 60
        sec = (self.sec % 3600) % 60
        self.timeLabel.setText("%02d:%02d:%02d" % (hour, minut, sec))

    def exit(self):
        self.stop()
        self.firstTime = True
        self.random_pic()
        self.mainMenu.show()
        self.timer.stop()
        self.sec = 0
        self.set_time()
        self.random_pic()
        self.makeAllDefault()
        self.wrongsNumber.display(self.errors)
        self.close()

    def addMenu(self, mainMenu):
        self.mainMenu = mainMenu


class MemoryTraining(QObject):
    def __init__(self):
        super().__init__()
        self.mainMenu = MainMenu()
        self.mainMenu.show()
        self.mainMenu.setEnabled(False)
        
        self.game = Game()
        self.game.addMenu(self.mainMenu)
        self.mainMenu.addGame(self.game)
        self.bd = dict()
        self.bd["1234"] = "1234"

        self.autorization = Autorization()
        self.autorization.addMenu(self.mainMenu)
        self.autorization.addBd(self.bd)
        self.autorization.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MemoryTraining()
    sys.exit(app.exec_())