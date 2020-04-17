import os
import sys
import time
import win32api
import shutil
import threading
import requests
import zipfile
import smtplib as smtp
from ui.untitled1 import *
from ui.untitled2 import *
from ui.untitled3 import *
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox


def winMinimize():
    for i in range(100, 0, -1):
        window.setWindowOpacity(i / 100)
        time.sleep(0.01)
    window.showMinimized()
    window.setWindowOpacity(1)


def sendEMail(text):
    email = 'VladimirKurdiukovv@yandex.ru'
    password = 'fwducjdmhibwpvto'
    dest_email = 'system.copyrightlava@gmail.com'
    subject = "this is servise message from Lava controller"
    email_text = text

    message = 'From: {}\nTo: {}\nSubject: {}\n\n{}'.format(email,
                                                           dest_email,
                                                           subject,
                                                           email_text)

    server = smtp.SMTP_SSL('smtp.yandex.com')
    # server.set_debuglevel(1)
    server.ehlo(email)
    server.login(email, password)
    server.auth_plain()
    server.sendmail(email, dest_email, message)
    server.quit()


def download(fr, to):
    f = open(to, "wb")  # открываем файл для записи, в режиме wb
    ufr = requests.post(fr)  # делаем запрос
    f.write(ufr.content)  # записываем содержимое в файл; как видите - content запроса
    f.close()


def checkClosed():
    if not power:
        raise SystemExit


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow1()
        self.ui.setupUi(self)


class MyWin2(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow2()
        self.ui.setupUi(self)


class MyWin3(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow3()
        self.ui.setupUi(self)


def errorMsg(title, text):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    # msg.setIconPixmap(pixmap)  # Своя картинка

    msg.setWindowTitle("Ошибка!")
    msg.setText(title)
    msg.setInformativeText(text)
    # msg.setDetailedText("DetailedText")

    okButton = msg.addButton('Ok', QMessageBox.AcceptRole)

    msg.exec()


def stopApp():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    # msg.setIconPixmap(pixmap)  # Своя картинка

    msg.setWindowTitle("Информация")
    msg.setText("Внимание!")
    msg.setInformativeText("Вы уверены, что хотите прервать установку?")
    # msg.setDetailedText("DetailedText")

    okButton = msg.addButton('Да', QMessageBox.AcceptRole)
    msg.addButton('Нет, продолжить.', QMessageBox.RejectRole)

    msg.exec()
    if msg.clickedButton() == okButton:
        print("Close")
        global power
        power = False
        for i in createdFiles:
            os.remove(i)
        raise SystemExit
    else:
        print("No")


def stop():
    print("stop1")
    window.close()
    print("stop")
    raise SystemExit


def point3():
    print(31)
    global Text
    print(32)

    def tryDel(pat):
        try:
            os.remove(pat)
        except FileNotFoundError:
            pass


    def install():

        window.ui.pushButton.setText("Ждите")

        def addFile(pat):
            createdFiles.append(os.path.abspath(pat))

        def remFile(pat):
            global createdFiles
            createdFiles.pop(createdFiles.index(os.path.abspath(pat)))


        try:

            # Отсюда начинается установка программы

            upText("Распаковка архивов")
            shutil.copy("data\\lava.zip", "data.zip")
            addFile("data.zip")
            # setProgress(18)
            f = zipfile.ZipFile("data.zip")
            f.extractall(pwd=b"lavastudioistop")
            # setProgress(25)
            addFile("controller.zip")
            if os.path.exists("controller.zip"):
                upText("Модуль контроля загружен")
            else:
                upText("!Модуль контроля загружен с ошибкой")
            # setProgress(40)
            upText("Распаковка модуля контроля")
            f = zipfile.ZipFile("controller.zip")
            f.extractall()
            addFile("controller.exe")
            upText("Распаковка модуля контроля завершена")
            # window.ui.progressBar.setValue(70)
            upText("Подготовка дистрибутивов")
            try:
                os.makedirs(path)
            except:
                pass
            tryDel("C:\\Users\\{}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\controller.exe".format(os.environ.get("USERNAME")))
            tryDel("C:\\Users\\{}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\LavaController.exe".format(os.environ.get("USERNAME")))

            upText("Копирование файлов")
            addFile("C:\\Users\\{}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\controller.exe".format(os.environ.get("USERNAME")))
            shutil.copy("controller.exe", "C:\\Users\\{}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\controller.exe".format(os.environ.get("USERNAME")))
            # os.rename("C:\\Users\\{}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\controller.exe".format(os.environ.get("USERNAME"), "C:\\Users\\{}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\LavaController.exe".format(os.environ.get("USERNAME"))))

            upText("Очистка кэша")
            try:
                del f
                os.remove("controller.zip")
                os.remove("data.zip")
                os.remove("controller.exe")
                remFile("controller.zip")
            except BaseException:
                upText("Произошла не фатальная ошибка при очистке кэш данных")
            else:
                upText("Кэш данные удалены успешно")

            # Здесь установка завершается

        except BaseException:
            del f
            upText("!Ошибка установки")
            upText("!Откат!") # --uac-admin
            for i in createdFiles:
                upText("del: " + i)
                time.sleep(0.2)
            print(createdFiles)
            global power
            power = False
            for i in createdFiles:
                os.remove(i)
            QMessageBox.warning(window, "Fatal Error", "Произошла фатальная ошибка при устаноке программы.\nБыл выполнен откат установки, не закрывайте программу",
                                QMessageBox.Ok)
            raise SystemExit
        upText("Установка завершена без критических ошибок")
        window.ui.pushButton.setText("Закончить")
        window.ui.pushButton.clicked.connect(window.close)
        # setProgress(100)

        pass


    def upText(txt):
        global Text
        Text += txt + "\n"
        window.ui.textBrowser.setText(Text)
        window.ui.textBrowser.adjustSize()

    global window
    window.close()
    window = MyWin3()  # Создаем окно (именно в окне отображаются все виджеты)
    window.setWindowFlags(Qt.FramelessWindowHint)
    window.ui.closeButton.clicked.connect(stopApp)
    window.ui.minimizeButton.clicked.connect(winMinimize)
    ins = threading.Thread(target=install)
    ins.start()
    # window.ui.pushButton.setCheckable(False)
    window.show()
    app.exec_()
    checkClosed()


def point2():
    def point3test():
        if os.path.isabs(path):
            r = win32api.GetDiskFreeSpace(r'{}:'.format(path[0]))
            free_space = r[0] * r[1] * r[2] / 1024 / 1024
            if free_space > PROGRAMM_DISTRIBUTIVE_WEIGHT:
                print(3)
                point3()
            else:
                errorMsg("Недостаточно места на диске!", "Для установки необходимо - {}Мб свободного места.\n На ди\
ске '{}' Доступно - {}Мб".format(PROGRAMM_DISTRIBUTIVE_WEIGHT, path[0], round(free_space, 2)))
        else:
            errorMsg("Неверно указан путь!",
                     "Путь '{}' не является ссылкой на дирректорию.".format(path))

    def getNewPath():
        global path
        path = os.path.normpath(QtWidgets.QFileDialog.getExistingDirectory(window, "Выбрать папку", ".")) + "\\LavaStudio"
        print(path, 2.5)
        if path != "" and path != ".\\LavaStudio":
            window.ui.lineEdit.setText(path)
            print(r'{}:'.format(path[0]))
            r = win32api.GetDiskFreeSpace(r'{}:'.format(path[0]))
            free_space = r[0] * r[1] * r[2] / 1024 / 1024
            window.ui.label_5.setText(" На выбраном диске доступно {}Мб сободного места".format(free_space))
        else:
            path = "C:\\LavaStudio"

    global path
    path = "C:\\LavaStudio"
    global window
    window.close()
    window = MyWin2()  # Создаем окно (именно в окне отображаются все виджеты)
    window.setWindowFlags(Qt.FramelessWindowHint)
    window.ui.closeButton.clicked.connect(stopApp)
    window.ui.pushButton_2.clicked.connect(getNewPath)
    window.ui.lineEdit.setText(path)
    window.ui.minimizeButton.clicked.connect(winMinimize)
    window.ui.pushButton.clicked.connect(point3test)
    r = win32api.GetDiskFreeSpace(r'{}:'.format(path[0]))
    free_space = r[0] * r[1] * r[2] / 1024 / 1024
    window.ui.label_4.setText(" Необходимо минимум {}Мб свободного места".format(PROGRAMM_DISTRIBUTIVE_WEIGHT))
    window.ui.label_5.setText(" На выбраном диске доступно {}Мб сободного места".format(round(free_space, 2)))
    window.ui.lineEdit.setReadOnly(True)
    window.show()
    app.exec_()
    checkClosed()


def passing():
    pass


def point1():
    global CBState
    CBState = False

    def checkBocksClicked():
        global CBState
        if CBState:
            CBState = False
        else:
            CBState = True

    def point2test():
        global CBState
        if CBState:
            point2()
        else:
            window.ui.checkBox.setStyleSheet("border: 4px double red; padding 5px;")

    global window, app
    app = QtWidgets.QApplication(sys.argv)  # Создаем приложение (программы)
    window = MyWin()  # Создаем окно (именно в окне отображаются все виджеты)
    window.setWindowFlags(Qt.FramelessWindowHint)
    window.ui.closeButton.clicked.connect(stopApp)
    window.ui.pushButton.clicked.connect(point2test)
    window.ui.minimizeButton.clicked.connect(winMinimize)
    window.ui.textBrowser.setText(USER_AGREEMENT)
    window.ui.checkBox.clicked.connect(checkBocksClicked)
    window.show()
    app.exec_()


TextN = 1
Text = ""
PROGRAMM_DISTRIBUTIVE_WEIGHT = 100
path = "C:\\LavaStudio"
USER_AGREEMENT = """<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n
<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n
p, li { white-space: pre-wrap; }\n
</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:600; font-style:italic; color:#888888;\">Добро пожаловать!</span></p>\n
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; color:#888888;\">Вас приветствует мастер установки Lava Studio.</span></p>\n
<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8pt; color:#888888;\"><br /></p>\n
<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:600; text-decoration: underline;\">Пользовательское соглашение:</span></p>
<p>В далеком-далеком предалеком будущем тут возможно когда-нибудь появится это самое соглашение.</p></body></html>"""

power = True
createdFiles = []
point1()
