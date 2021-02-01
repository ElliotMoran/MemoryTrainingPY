import sqlite3
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QGridLayout, QLineEdit, QWidget


class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('resources/ui/mainMenu.ui', self)
        self.setFixedSize(1280, 720)
        self.move(0, 0)

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
        self.checkBox.stateChanged.connect(self.showHidePassword)

    def addAuto(self, auto):
        self.autorization = auto

    def exit(self):
        sys.exit()

    def startGame(self):
        self.hide()
        self.game.show()
        self.game.setEnabled(True)

    def addGame(self, game):
        self.game = game

    def showHidePassword(self):
        if self.checkBox.checkState():
            self.newPasswordEdit.setEchoMode(QLineEdit.Normal)
        else:
            self.newPasswordEdit.setEchoMode(QLineEdit.Password)

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
            self.errorsPasswordLabel.setText('Password changed successfully')
        else:
            self.errorsPasswordLabel.setText('Less than 6 symbols')

    # показ кнопок смены пароля
    def showPassChange(self):
        self.changePasswordButton.hide()
        self.frameNewPassword.show()
        self.returnButton.show()

    # показ рейтинга
    def showRating(self):
        # показ лучшего результата авторизированного пользователя
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

        # показ рейтинг всех пользователей
        tempLayout = QGridLayout()
        tempWidget = QWidget()
        users = list()
        sql.execute(
            f"SELECT login, time, mistakes FROM users")
        users = list(sql.fetchall())
        for i in range(len(users)):
            users[i] = list(users[i])
        users.sort(key=lambda x: 1000 - x[1] - x[2] * 5)
        users.reverse()
        for i in range(len(users)):
            for j in range(len(users[i])):
                tempLine = QLineEdit(str(users[i][j]))
                tempLine.setReadOnly(True)
                tempLayout.addWidget(tempLine, i, j)
        tempWidget.setLayout(tempLayout)
        self.scrollArea.setWidget(tempWidget)

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
