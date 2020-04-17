# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\controller\ui\untitled3.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import os
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow3(object):
    def setupUi(self, MainWindow3):
        MainWindow3.setObjectName("MainWindow3")
        MainWindow3.resize(500, 400)
        MainWindow3.setMinimumSize(QtCore.QSize(500, 400))
        MainWindow3.setMaximumSize(QtCore.QSize(500, 400))
        MainWindow3.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow3)
        self.centralwidget.setObjectName("centralwidget")
        self.backgrownd = QtWidgets.QLabel(self.centralwidget)
        self.backgrownd.setGeometry(QtCore.QRect(0, 0, 500, 400))
        self.backgrownd.setText("")
        self.backgrownd.setPixmap(QtGui.QPixmap(os.getcwd() + "/media/backgrownd.png"))
        self.backgrownd.setObjectName("backgrownd")
        self.minimizeButton = QtWidgets.QPushButton(self.centralwidget)
        self.minimizeButton.setGeometry(QtCore.QRect(445, 0, 25, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.minimizeButton.setFont(font)
        self.minimizeButton.setStyleSheet("background-color: rgba(0, 0, 0, 50);\n"
"color: rgb(255, 255, 255);")
        self.minimizeButton.setObjectName("minimizeButton")
        self.closeButton = QtWidgets.QPushButton(self.centralwidget)
        self.closeButton.setGeometry(QtCore.QRect(475, 0, 25, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.closeButton.setFont(font)
        self.closeButton.setStyleSheet("background-color: rgba(0, 0, 0, 50);\n"
"color: rgb(255, 255, 255);")
        self.closeButton.setObjectName("closeButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(479, 60, 3, 30))
        self.label.setStyleSheet("background-color: rgb(160, 160, 159);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(374, 362, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("position: absolute;\n"
"left: 0%;\n"
"right: 0%;\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(0, 63, 136, 255), stop:1 rgba(0, 150, 244, 200));\n"
"border: none;\n"
"color: rgb(254, 251, 255);")
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 150, 461, 61))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(160, 160, 159);")
        self.label_3.setObjectName("label_3")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(30, 200, 331, 191))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 329, 189))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.textBrowser = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 331, 191))
        self.textBrowser.setText("")
        self.textBrowser.setObjectName("textBrowser")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(290, 40, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(160, 160, 159);")
        self.label_6.setObjectName("label_6")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(290, 70, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(160, 160, 159);")
        self.label_2.setObjectName("label_2")
        MainWindow3.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow3)

    def retranslateUi(self, MainWindow3):
        _translate = QtCore.QCoreApplication.translate
        MainWindow3.setWindowTitle(_translate("MainWindow3", "MainWindow"))
        self.minimizeButton.setText(_translate("MainWindow3", "-"))
        self.closeButton.setText(_translate("MainWindow3", "x"))
        self.pushButton.setText(_translate("MainWindow3", "Продолжить"))
        self.label_3.setText(_translate("MainWindow3", "Идет загрузка и развертывание дистрибутивов:"))
        self.label_6.setText(_translate("MainWindow3", "Сейчас происходит:"))
        self.label_2.setText(_translate("MainWindow3", "Установка..."))
