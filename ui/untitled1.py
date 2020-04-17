# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\controller\ui\untitled1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import os
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow1(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 400)
        MainWindow.setMinimumSize(QtCore.QSize(500, 400))
        MainWindow.setMaximumSize(QtCore.QSize(500, 400))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
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
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(290, 70, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(160, 160, 159);")
        self.label_2.setObjectName("label_2")
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
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 180, 321, 161))
        self.textBrowser.setObjectName("textBrowser")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(30, 350, 251, 21))
        self.checkBox.setObjectName("checkBox")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(290, 40, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(160, 160, 159);")
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.minimizeButton.setText(_translate("MainWindow", "-"))
        self.closeButton.setText(_translate("MainWindow", "x"))
        self.label_2.setText(_translate("MainWindow", "Установка..."))
        self.pushButton.setText(_translate("MainWindow", "Продолжить"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#888888;\">Добро пожаловать!</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#888888;\">Вас приветствует мастер установки Lava Studio.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#888888;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600; text-decoration: underline;\">Пользовательское соглашение:</span></p></body></html>"))
        self.checkBox.setText(_translate("MainWindow", "Я принимаю пользовательское соглашение"))
        self.label_3.setText(_translate("MainWindow", "Сейчас происходит:"))
