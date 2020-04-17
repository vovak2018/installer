# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\controller\ui\untitled2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import os
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow2(object):
    def setupUi(self, MainWindow2):
        MainWindow2.setObjectName("MainWindow2")
        MainWindow2.resize(500, 400)
        MainWindow2.setMinimumSize(QtCore.QSize(500, 400))
        MainWindow2.setMaximumSize(QtCore.QSize(500, 400))
        MainWindow2.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow2)
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
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 220, 361, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 160, 461, 61))
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
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 220, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("position: absolute;\n"
"left: 0%;\n"
"right: 0%;\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(0, 63, 136, 255), stop:1 rgba(0, 150, 244, 200));\n"
"border: none;\n"
"color: rgb(254, 251, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 270, 491, 21))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(160, 160, 159);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 300, 461, 21))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(160, 160, 159);")
        self.label_5.setObjectName("label_5")
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
        MainWindow2.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow2)

    def retranslateUi(self, MainWindow2):
        _translate = QtCore.QCoreApplication.translate
        MainWindow2.setWindowTitle(_translate("MainWindow2", "MainWindow"))
        self.minimizeButton.setText(_translate("MainWindow2", "-"))
        self.closeButton.setText(_translate("MainWindow2", "x"))
        self.pushButton.setText(_translate("MainWindow2", "Продолжить"))
        self.lineEdit.setText(_translate("MainWindow2", "C:\\Program Files\\LavaStudio"))
        self.label_3.setText(_translate("MainWindow2", "Теперь выберете место для установки:"))
        self.pushButton_2.setText(_translate("MainWindow2", "Обзор..."))
        self.label_4.setText(_translate("MainWindow2", " Необходимо минимум 100Мб свободного места"))
        self.label_5.setText(_translate("MainWindow2", " На выбраном диске доступно 100Мб сободного места"))
        self.label_6.setText(_translate("MainWindow2", "Сейчас происходит:"))
        self.label_2.setText(_translate("MainWindow2", "Установка..."))
