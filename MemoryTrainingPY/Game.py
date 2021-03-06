import sqlite3
import random
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QLineEdit
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap
from ClickedLabel import ClickedLabel


class Game(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("resources/ui/game.ui", self)
        self.setFixedSize(1280, 720)
        self.move(0, 0)

        self.userName = None

        self.setupUi()

        self.errors = 0
        self.mainMenu = None
        self.winWindow = None
        self.firstTime = True

        self.sec = 0
        self.timer = QTimer()
        self.setTime()
        self.timer.timeout.connect(self.counter)

        self.randomPic()
        self.makeAllOff()
        self.makeAllDefault()

        self.startButton.clicked.connect(self.start)
        self.stopButton.clicked.connect(self.stop)
        self.exitButton.clicked.connect(self.exit)

        for el in self.labels:
            el.clicked.connect(self.nothing)

    def setupUi(self):
        self.picPart_1 = ClickedLabel()
        self.gridLayout.addWidget(self.picPart_1, 0, 0, 1, 1)
        self.picPart_2 = ClickedLabel()
        self.gridLayout.addWidget(self.picPart_2, 0, 1, 1, 1)
        self.picPart_3 = ClickedLabel()
        self.gridLayout.addWidget(self.picPart_3, 0, 2, 1, 1)
        self.picPart_4 = ClickedLabel()
        self.gridLayout.addWidget(self.picPart_4, 0, 3, 1, 1)
        self.picPart_5 = ClickedLabel()
        self.gridLayout.addWidget(self.picPart_5, 1, 0, 1, 1)
        self.picPart_6 = ClickedLabel()
        self.gridLayout.addWidget(self.picPart_6, 1, 1, 1, 1)
        self.picPart_7 = ClickedLabel()
        self.gridLayout.addWidget(self.picPart_7, 1, 2, 1, 1)
        self.picPart_8 = ClickedLabel()
        self.gridLayout.addWidget(self.picPart_8, 1, 3, 1, 1)
        self.picPart_9 = ClickedLabel()
        self.gridLayout.addWidget(self.picPart_9, 2, 0, 1, 1)
        self.picPart_10 = ClickedLabel()
        self.gridLayout.addWidget(self.picPart_10, 2, 1, 1, 1)
        self.picPart_11 = ClickedLabel()
        self.gridLayout.addWidget(self.picPart_11, 2, 2, 1, 1)
        self.picPart_12 = ClickedLabel()
        self.gridLayout.addWidget(self.picPart_12, 2, 3, 1, 1)
        self.picPart_13 = ClickedLabel()
        self.gridLayout.addWidget(self.picPart_13, 3, 0, 1, 1)
        self.picPart_14 = ClickedLabel()
        self.gridLayout.addWidget(self.picPart_14, 3, 1, 1, 1)
        self.picPart_15 = ClickedLabel()
        self.gridLayout.addWidget(self.picPart_15, 3, 2, 1, 1)
        self.picPart_16 = ClickedLabel()
        self.gridLayout.addWidget(self.picPart_16, 3, 3, 1, 1)
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

        self.pics = ["resources/pics/auto1.jpeg", "resources/pics/auto2.jpeg", "resources/pics/auto3.jpeg", "resources/pics/auto4.jpeg",
                     "resources/pics/auto5.jpeg", "resources/pics/auto6.jpeg", "resources/pics/auto7.jpeg", "resources/pics/auto8.jpeg",
                     "resources/pics/auto1.jpeg", "resources/pics/auto2.jpeg", "resources/pics/auto3.jpeg", "resources/pics/auto4.jpeg",
                     "resources/pics/auto5.jpeg", "resources/pics/auto6.jpeg", "resources/pics/auto7.jpeg", "resources/pics/auto8.jpeg"]

        self.labels = [self.picPart_1, self.picPart_2, self.picPart_3, self.picPart_4,
                       self.picPart_5, self.picPart_6, self.picPart_7, self.picPart_8,
                       self.picPart_9, self.picPart_10, self.picPart_11, self.picPart_12,
                       self.picPart_13, self.picPart_14, self.picPart_15, self.picPart_16]

        for el in self.labels:
            el.hide()

    # сделал так, так как при setEnabled(False) виджеты окрашивются в серый, а замена на функцию nothing() это исправляет
    def reconnect(self, signal, newhandler=None, oldhandler=None):
        while True:
            try:
                if oldhandler is not None:
                    signal.disconnect(oldhandler)
                else:
                    signal.disconnect()
            except TypeError:
                break
        if newhandler is not None:
            signal.connect(newhandler)

    # пустая функция чтобы реализовать аналог setEnabled(False)
    def nothing(self):
        pass

    def addWinWindow(self, winWindow):
        self.winWindow = winWindow

    # перемешивание картинок
    def randomPic(self):
        random.shuffle(self.pics)

    # замена всех picLabel на работающую функцию
    def makeAllOn(self):
        for el in self.labels:
            self.reconnect(el.clicked, self.picClicked)

    # замена всех picLabel на пустую функцию
    def makeAllOff(self):
        for el in self.labels:
            self.reconnect(el.clicked, self.nothing)

    # замена всех картинок picLabel на дефолтную
    def makeAllDefault(self):
        for el in self.labels:
            el.setPixmap(QPixmap("resources/pics/default.jpeg"))

    # замена всех picLabel на их картинки
    def showAll(self):
        for el in self.labels:
            el.setPixmap(QPixmap(self.pics[int(el.getName()) - 1]))

    # проверка все ли картинки были найдены
    def checkAll(self):
        for el in self.labels:
            if not el.outOfGame:
                return False
        return True

    # показ 2 нажатых картинок и смена их на дефолтные
    def make2Default(self, el1, el2):
        def func():
            for el in self.labels:
                self.reconnect(el.clicked, self.picClicked)
                if el.outOfGame:
                    self.reconnect(el.clicked, self.nothing)
                    el.setPixmap(QPixmap("resources/pics/outofgame.jpeg"))
            if not el1.outOfGame:
                el1.setPixmap(QPixmap("resources/pics/default.jpeg"))
            if not el2.outOfGame:
                el2.setPixmap(QPixmap("resources/pics/default.jpeg"))
        return func

    # функция выполняется если нажата picLabel(картинка)
    def picClicked(self):
        sender = self.sender()
        if sender.wasClicked:
            return
        sender.wasClicked = True
        sender.setPixmap(QPixmap(self.pics[int(sender.getName()) - 1]))
        for el in self.labels:
            if sender == el:
                continue
            if el.wasClicked:
                if self.pics[int(sender.getName()) - 1] == self.pics[int(el.getName()) - 1]:
                    self.makeAllOff()
                    self.timerScreen = QTimer()
                    self.timerScreen.setSingleShot(True)
                    self.timerScreen.timeout.connect(
                        self.make2Default(el, sender))
                    self.timerScreen.start(1500)
                    sender.wasClicked = False
                    el.wasClicked = False
                    sender.outOfGame = True
                    el.outOfGame = True
                else:
                    self.makeAllOff()
                    self.timerScreen = QTimer()
                    self.timerScreen.setSingleShot(True)
                    self.timerScreen.timeout.connect(
                        self.make2Default(el, sender))
                    self.timerScreen.start(1500)
                    sender.wasClicked = False
                    el.wasClicked = False
                    self.errors += 1
                    self.wrongsNumber.display(self.errors)

        # если все пары были найдены
        if self.checkAll():
            self.userName = self.mainMenu.autorization.getUserName()
            self.winWindow.show()
            self.setEnabled(False)
            hour = self.sec / 3600
            minut = (self.sec % 3600) / 60
            sec = (self.sec % 3600) % 60
            self.winWindow.timeLabel.setText(
                "%02d:%02d:%02d" % (hour, minut, sec))
            self.winWindow.errorsLabel.setText(str(self.errors))

            db = sqlite3.connect('MemoryTrainingDB.db')
            sql = db.cursor()
            sql.execute(
                f"SELECT time FROM users WHERE login = '{self.userName}'")
            bestTime = sql.fetchone()
            bestTime = int(list(bestTime)[0])
            sql.execute(
                f"SELECT mistakes FROM users WHERE login = '{self.userName}'")
            bestErrors = sql.fetchone()
            bestErrors = int(list(bestErrors)[0])
            if 1000 - bestTime - bestErrors * 5 < 1000 - self.sec - self.errors * 5:
                sql.execute(
                    f"UPDATE users SET time = {self.sec} WHERE login = '{self.userName}'")
                db.commit()
                sql.execute(
                    f"UPDATE users SET mistakes = {self.errors} WHERE login = '{self.userName}'")
                db.commit()
            self.stop()

    # кнопка старта
    def start(self):
        # если кнопка была нажата впервый раз
        if self.firstTime:
            self.firstTime = False
            for el in self.labels:
                el.show()
            self.timerScreen = QTimer()
            self.timerScreen.setSingleShot(True)
            self.timerScreen.timeout.connect(self.makeAllDefault)
            self.timerScreen.start(5000)
            self.timerScreen1 = QTimer()
            self.timerScreen1.setSingleShot(True)
            self.timerScreen1.timeout.connect(self.makeAllOn)
            self.timerScreen1.start(5000)
            self.wrongsNumber.display(self.errors)
            self.showAll()
        else:
            self.makeAllOn()
            for el in self.labels:
                if el.outOfGame:
                    self.reconnect(el.clicked, self.nothing)
                    el.setPixmap(QPixmap("resources/pics/outofgame.jpeg"))
        self.timer.start(1000)

    def stop(self):
        for el in self.labels:
            el.wasClicked = False
        self.timer.stop()
        self.makeAllDefault()
        self.makeAllOff()

    def counter(self):
        self.sec += 1
        self.setTime()

    def setTime(self):
        hour = self.sec / 3600
        minut = (self.sec % 3600) / 60
        sec = (self.sec % 3600) % 60
        self.timeLabel.setText("%02d:%02d:%02d" % (hour, minut, sec))

    def exit(self):
        self.stop()
        for el in self.labels:
            el.hide()
            el.outOfGame = False
            el.wasClicked = False
        self.firstTime = True
        self.randomPic()
        self.mainMenu.show()
        self.timer.stop()
        self.sec = 0
        self.errors = 0
        self.setTime()
        self.randomPic()
        self.makeAllDefault()
        self.wrongsNumber.display(self.errors)
        self.makeAllOff()
        self.hide()

    def addMenu(self, mainMenu):
        self.mainMenu = mainMenu
