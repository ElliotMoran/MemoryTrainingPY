import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QLineEdit


class Autorization(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('resources/ui/authorization.ui', self)
        self.setFixedSize(740, 360)
        self.mainMenu = None
        self.check = False

        self.registerButton.clicked.connect(self.register)
        self.loginButton.clicked.connect(self.login)
        self.checkBox.stateChanged.connect(self.showHidePassword)
        self.userName = None
        self.move(10, 10)

    def getUserName(self):
        return self.userName

    def showHidePassword(self):
        if self.checkBox.checkState():
            self.passEdit.setEchoMode(QLineEdit.Normal)
        else:
            self.passEdit.setEchoMode(QLineEdit.Password)

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
                    f"""INSERT INTO users VALUES (?, ?, ?, ?)""", (name, password, 99999, 99999))
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
