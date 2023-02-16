import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from check_db import *
from loginn import *
from regisration import *

class InterfaceReg(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form2()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.reg)
        self.base_line_edit = [self.ui.lineEdit, self.ui.lineEdit_2, self.ui.lineEdit_3,
        self.ui.lineEdit_4, self.ui.lineEdit_5]

        self.check_db = CheckThread()
        self.check_db.mysignal.connect(self.signal_handler)

# проверка правильности ввода
    def check_input(funct):
        def wrapper(self):
            for line_edit in self.base_line_edit:
                if len(line_edit.text()) == 0:
                    return
            funct(self)

        return wrapper



    @check_input
    def reg(self):
        fio = self.ui.lineEdit.text()
        post = self.ui.dateEdit_2.text()
        name= self.ui.lineEdit_3.text()
        passw = self.ui.lineEdit_4.text()
        role = self.ui.lineEdit_5.text()
        self.check_db.thr_register(fio, post, name, passw, role)

class InterfaceMain(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form1()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.auth)

        self.base_line_edit = [self.ui.lineEdit, self.ui.lineEdit_2]

        self.check_db = CheckThread()
        self.check_db.mysignal.connect(self.signal_handler)



    class InterfaceAuth(QtWidgets.QWidget):
        def __init__(self, parent=None):
            super().__init__(parent)
            self.ui = Ui_Form1()
            self.ui.setupUi(self)

            self.ui.pushButton.clicked.connect(self.auth)
            self.ui.pushButton.clicked.connect(self.)

            self.base_line_edit = [self.ui.lineEdit, self.ui.lineEdit_2]

            self.check_db = CheckThread()
            self.check_db.mysignal.connect(self.signal_handler)

# проверка правильности ввода
    def check_input(funct):
        def wrapper(self):
            for line_edit in self.base_line_edit:
                if len(line_edit.text()) == 0:
                    return
            funct(self)

        return wrapper

# обработчик сигналов
    def signal_handler(self, value):
        QtWidgets.QMessageBox.about(self, 'Оповещение', value)
        if value == "Авторизация успешна!":
            self.im.show()
            self.close()

    @check_input
    def auth(self):
        name = self.ui.lineEdit.text()
        passw = self.ui.lineEdit_2.text()
        self.check_db.thr_login(name, passw)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mywin = InterfaceMain()
    mywin.show()
    sys.exit(app.exec_())