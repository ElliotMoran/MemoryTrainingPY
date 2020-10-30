from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainMenuWindow(object):
    def setupUi(self, MainMenuWindow):
        MainMenuWindow.setObjectName("MainMenuWindow")
        MainMenuWindow.resize(1280, 720)
        self.centralwidget = QtWidgets.QWidget(MainMenuWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(550, 180, 160, 80))
        self.startButton.setObjectName("startButton")
        self.ratingButton = QtWidgets.QPushButton(self.centralwidget)
        self.ratingButton.setGeometry(QtCore.QRect(550, 270, 160, 80))
        self.ratingButton.setObjectName("ratingButton")
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(550, 360, 160, 80))
        self.exitButton.setObjectName("exitButton")
        MainMenuWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainMenuWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 20))
        self.menubar.setObjectName("menubar")
        MainMenuWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainMenuWindow)
        self.statusbar.setObjectName("statusbar")
        MainMenuWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainMenuWindow)
        QtCore.QMetaObject.connectSlotsByName(MainMenuWindow)

        self.exitButton.clicked.connect(self.exit)


    def exit(self):
        sys.exit()

    def retranslateUi(self, MainMenuWindow):
        _translate = QtCore.QCoreApplication.translate
        MainMenuWindow.setWindowTitle(_translate("MainMenuWindow", "MainWindow"))
        self.startButton.setText(_translate("MainMenuWindow", "Start"))
        self.ratingButton.setText(_translate("MainMenuWindow", "Rating"))
        self.exitButton.setText(_translate("MainMenuWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainMenuWindow = QtWidgets.QMainWindow()
    ui = Ui_MainMenuWindow()
    ui.setupUi(MainMenuWindow)
    MainMenuWindow.show()
    sys.exit(app.exec_())
