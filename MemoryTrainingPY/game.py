# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'game.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 30, 511, 351))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.picPart_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.picPart_3.setObjectName("picPart_3")
        self.gridLayout.addWidget(self.picPart_3, 0, 2, 1, 1)
        self.picPart_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.picPart_2.setObjectName("picPart_2")
        self.gridLayout.addWidget(self.picPart_2, 0, 1, 1, 1)
        self.picPart_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.picPart_5.setObjectName("picPart_5")
        self.gridLayout.addWidget(self.picPart_5, 1, 0, 1, 1)
        self.picPart_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.picPart_4.setObjectName("picPart_4")
        self.gridLayout.addWidget(self.picPart_4, 0, 3, 1, 1)
        self.picPart_15 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.picPart_15.setObjectName("picPart_15")
        self.gridLayout.addWidget(self.picPart_15, 3, 2, 1, 1)
        self.picPart_16 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.picPart_16.setObjectName("picPart_16")
        self.gridLayout.addWidget(self.picPart_16, 3, 3, 1, 1)
        self.picPart_14 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.picPart_14.setObjectName("picPart_14")
        self.gridLayout.addWidget(self.picPart_14, 3, 1, 1, 1)
        self.picPart_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.picPart_13.setObjectName("picPart_13")
        self.gridLayout.addWidget(self.picPart_13, 3, 0, 1, 1)
        self.picPart_1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.picPart_1.setObjectName("picPart_1")
        self.gridLayout.addWidget(self.picPart_1, 0, 0, 1, 1)
        self.picPart_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.picPart_12.setObjectName("picPart_12")
        self.gridLayout.addWidget(self.picPart_12, 2, 3, 1, 1)
        self.picPart_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.picPart_9.setObjectName("picPart_9")
        self.gridLayout.addWidget(self.picPart_9, 2, 0, 1, 1)
        self.picPart_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.picPart_8.setObjectName("picPart_8")
        self.gridLayout.addWidget(self.picPart_8, 1, 3, 1, 1)
        self.picPart_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.picPart_11.setObjectName("picPart_11")
        self.gridLayout.addWidget(self.picPart_11, 2, 2, 1, 1)
        self.picPart_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.picPart_6.setObjectName("picPart_6")
        self.gridLayout.addWidget(self.picPart_6, 1, 1, 1, 1)
        self.picPart_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.picPart_7.setObjectName("picPart_7")
        self.gridLayout.addWidget(self.picPart_7, 1, 2, 1, 1)
        self.picPart_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.picPart_10.setObjectName("picPart_10")
        self.gridLayout.addWidget(self.picPart_10, 2, 1, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(570, 30, 160, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.wrongsText = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.wrongsText.setFont(font)
        self.wrongsText.setObjectName("wrongsText")
        self.horizontalLayout.addWidget(self.wrongsText)
        self.wrongsNumber = QtWidgets.QLCDNumber(self.horizontalLayoutWidget)
        self.wrongsNumber.setObjectName("wrongsNumber")
        self.horizontalLayout.addWidget(self.wrongsNumber)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(570, 130, 160, 151))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.startButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.startButton.setFont(font)
        self.startButton.setObjectName("startButton")
        self.verticalLayout.addWidget(self.startButton)
        self.stopButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.stopButton.setFont(font)
        self.stopButton.setObjectName("stopButton")
        self.verticalLayout.addWidget(self.stopButton)
        self.exitButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.exitButton.setFont(font)
        self.exitButton.setObjectName("exitButton")
        self.verticalLayout.addWidget(self.exitButton)
        self.timeLabel = QtWidgets.QLabel(self.centralwidget)
        self.timeLabel.setGeometry(QtCore.QRect(570, 80, 161, 31))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.timeLabel.setFont(font)
        self.timeLabel.setObjectName("timeLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.picPart_3.setText(_translate("MainWindow", "3"))
        self.picPart_2.setText(_translate("MainWindow", "2"))
        self.picPart_5.setText(_translate("MainWindow", "5"))
        self.picPart_4.setText(_translate("MainWindow", "4"))
        self.picPart_15.setText(_translate("MainWindow", "15"))
        self.picPart_16.setText(_translate("MainWindow", "16"))
        self.picPart_14.setText(_translate("MainWindow", "14"))
        self.picPart_13.setText(_translate("MainWindow", "13"))
        self.picPart_1.setText(_translate("MainWindow", "1"))
        self.picPart_12.setText(_translate("MainWindow", "12"))
        self.picPart_9.setText(_translate("MainWindow", "9"))
        self.picPart_8.setText(_translate("MainWindow", "8"))
        self.picPart_11.setText(_translate("MainWindow", "11"))
        self.picPart_6.setText(_translate("MainWindow", "6"))
        self.picPart_7.setText(_translate("MainWindow", "7"))
        self.picPart_10.setText(_translate("MainWindow", "10"))
        self.wrongsText.setText(_translate("MainWindow", "Wrongs:"))
        self.startButton.setText(_translate("MainWindow", "START"))
        self.stopButton.setText(_translate("MainWindow", "PAUSE"))
        self.exitButton.setText(_translate("MainWindow", "EXIT"))
        self.timeLabel.setText(_translate("MainWindow", "00:00:00"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
