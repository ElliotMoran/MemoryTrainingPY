import sys
import random
import sqlite3


from PyQt5 import uic
from PyQt5.Qt import pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel
from PyQt5.QtGui import *
from PyQt5.QtCore import *


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


class Autorization(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('authorization.ui', self)
        self.setFixedSize(740, 360)
        self.mainMenu = None
        self.check = False

        self.registerButton.clicked.connect(self.register)
        self.loginButton.clicked.connect(self.login)
        self.userName = None

    def getUserName(self):
        return self.userName

    # регистрация
    def register(self):
        db = sqlite3.connect('MemoryTrainingDB.db')
        sql = db.cursor()

        sql.execute("""CREATE TABLE IF NOT EXISTS users(
            login TEXT, 
            password TEXT,
            time BIGINT,
            mistakes BIGINT
        )""")
        db.commit()
        name = self.nickEdit.text()
        password = self.passEdit.text()
        if len(name) < 6:
            self.warningLabel.setText('Too small login!')
            self.nickEdit.setText('')
            self.passEdit.setText('')
        elif len(password) < 6:
            self.warningLabel.setText('Too small password!')
            self.nickEdit.setText('')
            self.passEdit.setText('')
        else:
            sql.execute(f"""SELECT login FROM users WHERE login = '{name}'""")
            if sql.fetchone() is None:
                sql.execute(
                    f"""INSERT INTO users VALUES (?, ?, ?, ?)""", (name, password, 0, 0))
                db.commit()
                self.check = True
                self.userName = name
                self.mainMenu.setEnabled(True)
                self.close()
            else:
                self.warningLabel.setText('User is already registered!')

    def login(self):
        db = sqlite3.connect('MemoryTrainingDB.db')
        sql = db.cursor()
        sql.execute("""CREATE TABLE IF NOT EXISTS users (
            login TEXT, 
            password TEXT,
            time BIGINT,
            mistakes BIGINT
        )""")
        db.commit()

        name = self.nickEdit.text()
        self.userName = name
        password = self.passEdit.text()

        sql.execute(f"""SELECT login FROM users WHERE login = '{name}'""")
        if sql.fetchone() is None:
            self.warningLabel.setText('User is not registered')
        else:
            sql.execute(
                f"""SELECT password FROM users WHERE password = '{password}' AND login = '{name}'""")
            if sql.fetchone() is None:
                self.warningLabel.setText('Wrong password!')
                self.passEdit.setText('')
            else:
                self.check = True
                self.mainMenu.setEnabled(True)
                self.close()

    def checkAutorization(self):
        return self.check

    def addMenu(self, menu):
        self.mainMenu = menu


class WinWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('winWindow.ui', self)
        self.setFixedSize(740, 360)

        self.game = None
        self.exitButton.clicked.connect(self.exit)

    def addGame(self, game):
        self.game = game

    def exit(self):
        self.close()
        self.game.exit()


class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('mainMenu.ui', self)
        self.setFixedSize(1280, 720)

        self.game = None
        self.userName = None
        self.autorization = None

        self.changePasswordButton.hide()
        self.returnButton.hide()
        self.frameRating.hide()
        self.frameNewPassword.hide()

        self.startButton.clicked.connect(self.startGame)
        self.exitButton.clicked.connect(self.exit)
        self.settingsButton.clicked.connect(self.showSettings)
        self.returnButton.clicked.connect(self.showMainButtons)
        self.ratingButton.clicked.connect(self.showRating)
        self.changePasswordButton.clicked.connect(self.showPassChange)
        self.acceptButton.clicked.connect(self.passChange)

    def addAuto(self, auto):
        self.autorization = auto

    def exit(self):
        sys.exit()

    def startGame(self):
        self.close()
        self.game.show()
        self.game.setEnabled(True)

    def addGame(self, game):
        self.game = game

    # смена пароля
    def passChange(self):
        self.userName = self.autorization.getUserName()
        db = sqlite3.connect('MemoryTrainingDB.db')
        sql = db.cursor()
        userPassword = self.newPasswordEdit.text()
        if len(userPassword) > 5:
            sql.execute(
                f"""UPDATE users SET password = '{userPassword}' WHERE login = '{self.userName}'""")
            db.commit()
        else:
            self.errorsPasswordLabel.setText('Less than 6 symbols')

    # показ кнопок смены пароля
    def showPassChange(self):
        self.changePasswordButton.hide()
        self.frameNewPassword.show()
        self.returnButton.show()

    # показ рейтинга
    def showRating(self):
        self.userName = self.autorization.getUserName()
        self.startButton.hide()
        self.settingsButton.hide()
        self.ratingButton.hide()
        self.exitButton.hide()
        self.frameRating.show()
        self.returnButton.show()
        db = sqlite3.connect('MemoryTrainingDB.db')
        sql = db.cursor()
        sql.execute(f"SELECT time FROM users WHERE login = '{self.userName}'")
        bestTime = sql.fetchone()
        bestTime = int(list(bestTime)[0])
        sql.execute(
            f"SELECT mistakes FROM users WHERE login = '{self.userName}'")
        bestErrors = sql.fetchone()
        bestErrors = int(list(bestErrors)[0])
        hour = bestTime / 3600
        minut = (bestTime % 3600) / 60
        sec = (bestTime % 3600) % 60
        self.timeLabel.setText("%02d:%02d:%02d" % (hour, minut, sec))
        self.errorsLabel.setText(str(bestErrors))

    # показ кнопок настроек
    def showSettings(self):
        self.changePasswordButton.show()
        self.returnButton.show()
        self.startButton.hide()
        self.settingsButton.hide()
        self.ratingButton.hide()
        self.exitButton.hide()

    # показ основных кнопок
    def showMainButtons(self):
        self.changePasswordButton.hide()
        self.frameRating.hide()
        self.returnButton.hide()
        self.frameNewPassword.hide()
        self.startButton.show()
        self.settingsButton.show()
        self.ratingButton.show()
        self.exitButton.show()


class Game(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("game.ui", self)
        self.setFixedSize(1280, 720)

        self.userName = None

        self.setupUi()

        self.errors = 0
        self.mainMenu = None
        self.winWindow = None
        self.firstTime = True

        self.sec = 0
        self.timer = QTimer()
        self.set_time()
        self.timer.timeout.connect(self.counter)

        self.random_pic()
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

        self.pics = ["pics/auto1.jpg", "pics/auto2.jpg", "pics/auto3.jpg", "pics/auto4.jpg",
                     "pics/auto5.jpg", "pics/auto6.jpg", "pics/auto7.jpg", "pics/auto8.jpg",
                     "pics/auto1.jpg", "pics/auto2.jpg", "pics/auto3.jpg", "pics/auto4.jpg",
                     "pics/auto5.jpg", "pics/auto6.jpg", "pics/auto7.jpg", "pics/auto8.jpg"]

        self.labels = [self.picPart_1, self.picPart_2, self.picPart_3, self.picPart_4,
                       self.picPart_5, self.picPart_6, self.picPart_7, self.picPart_8,
                       self.picPart_9, self.picPart_10, self.picPart_11, self.picPart_12,
                       self.picPart_13, self.picPart_14, self.picPart_15, self.picPart_16]

        for el in self.labels:
            el.hide()

    # сделал так как при setEnabled(False) виджеты окрашивются в серый, а замена на функцию nothing() это исправляет
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

    def random_pic(self):
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
            el.setPixmap(QPixmap("pics/default.jpg"))

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
                    el.setPixmap(QPixmap("pics/outofgame.jpg"))
            if not el1.outOfGame:
                el1.setPixmap(QPixmap("pics/default.jpg"))
            if not el2.outOfGame:
                el2.setPixmap(QPixmap("pics/default.jpg"))
        return func

    # функция выполняется если нажата picLabel
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
            if 0 == bestTime:
                sql.execute(
                    f"UPDATE users SET time = {self.sec} WHERE login = '{self.userName}'")
                db.commit()
            if 0 == bestErrors:
                sql.execute(
                    f"UPDATE users SET mistakes = {self.errors} WHERE login = '{self.userName}'")
                db.commit()
            if 1000 - bestTime - bestErrors * 5 < 1000 - self.sec - self.errors * 5:
                sql.execute(
                    f"UPDATE users SET time = {self.sec} WHERE login = '{self.userName}'")
                db.commit()
                sql.execute(
                    f"UPDATE users SET mistakes = {self.errors} WHERE login = '{self.userName}'")
                db.commit()
            self.stop()

    def start(self):
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
                    el.setPixmap(QPixmap("pics/outofgame.jpg"))
        self.timer.start(1000)

    def stop(self):
        for el in self.labels:
            el.wasClicked = False
        self.timer.stop()
        self.makeAllDefault()
        self.makeAllOff()

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
        for el in self.labels:
            el.hide()
            el.outOfGame = False
            el.wasClicked = False
        self.firstTime = True
        self.random_pic()
        self.mainMenu.show()
        self.timer.stop()
        self.sec = 0
        self.errors = 0
        self.set_time()
        self.random_pic()
        self.makeAllDefault()
        self.wrongsNumber.display(self.errors)
        self.makeAllOff()
        self.close()

    def addMenu(self, mainMenu):
        self.mainMenu = mainMenu


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
