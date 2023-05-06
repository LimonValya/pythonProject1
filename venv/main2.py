import sys
import threading

from PyQt5 import QtCore, QtGui, QtWidgets,QtSql
import mysql

from PyQt5.QtCore import Qt

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QApplication, QGridLayout, QWidget,QTableWidget, QTableWidgetItem, QComboBox


from loginn import *
from regisration import *
from  mainform import *
from check_db import *
from patient import *
from accept import *
from recording import *
from recipe import *
from redact_patient import *
from redact_worker import *
from nonee import *
from worker import *
from raspis_redd import *
from farma import *
class InterfaceReg(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form2()

        self.ui.setupUi(self)

        self.ui.pushButton_3.clicked.connect(self.reg)
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

# обработчик сигналов
    def signal_handler(self, value):
        QtWidgets.QMessageBox.about(self, 'Оповещение', value)

    @check_input
    def reg(self):
        fio = self.ui.lineEdit.text()
        post = self.ui.lineEdit_2.text()
        name = self.ui.lineEdit_3.text()
        passw = self.ui.lineEdit_4.text()
        role  = self.ui.lineEdit_5.text()
        self.check_db.thr_register(fio, post, name, passw, role)

class InterfaceMain(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.login = self.ui.label

        self.patient = InterfacePatient()
        self.recording = InterfaceRecording()
        self.raspis = InterfaceRaspis()
        self.accept = InterfaceAccept()
        self.recipe = InterfaceRecipe()
        self.redworker = InterfaceRedwork()
        self.worker = InterfaceWorker()
        self.redpatient = InterfaceRedpatient()
        self.record = InterfaceRecording

        self.ui.pushButton.clicked.connect(self.open_patient)
        self.ui.pushButton_2.clicked.connect(self.open_recording)
        self.ui.pushButton_3.clicked.connect(self.open_raspis)
        self.ui.pushButton_4.clicked.connect(self.open_accept)
        self.ui.pushButton_5.clicked.connect(self.open_recipe)
        self.ui.pushButton_7.clicked.connect(self.open_worker)
        self.ui.pushButton_8.clicked.connect(self.open_redpatient)
        self.ui.pushButton_9.clicked.connect(self.record)

        self.check_db = CheckThread()
        self.check_db.mysignal.connect(self.signal_handler)
        self.check_db.mysignal1.connect(self.signal_handler1)


    # def check(self):
    #     a=1
    #     self.check_db.thr_record(a)
    def open_patient(self):
        self.patient.show()

    def open_recording(self):
        self.recording.show()
        self.recording.check()

    def open_raspis(self):
        self.raspis.show()
        self.raspis.dbrapis()
    def open_accept(self):
        self.accept.show()

    def open_recipe(self):
        self.recipe.show()

    def open_worker(self):
        self.worker.show()
        self.worker.dbworker()

    def open_redpatient(self):
        self.redpatient.show()

    def open_record(self):
        self.record.show()
        self.record.check()

    def signal_handler(self, value):
        QtWidgets.QMessageBox.about(self, 'Оповещение', value)
    def check_input(funct):
        def wrapper(self):
            for line_edit in self.base_line_edit:
                if len(line_edit.text()) == 0:
                    return
            funct(self)
        return wrapper
    def reg_pacient(self):
        fio = self.ui.lineEdit_6.text()
        sex = self.ui.lineEdit_7.text()
        date = self.ui.lineEdit_8.text()
        address = self.ui.lineEdit_9.text()
        polis = self.ui.lineEdit_10.text()
        snils = self.ui.lineEdit_11.text()
        passport = self.ui.lineEdit_12.text()
        self.check_db.thr_patient(fio, sex, date, address, polis, snils, passport)

    def reg(self):
        fio = self.ui.lineEdit.text()
        post = self.ui.lineEdit_2.text()
        name = self.ui.lineEdit_3.text()
        passw = self.ui.lineEdit_4.text()
        role = self.ui.lineEdit_5.text()
        self.check_db.thr_register(fio, post, name, passw, role)

class InterfaceAuth(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.im = InterfaceMain()
        self.ui = Ui_Form1()
        self.ui.setupUi(self)

        self.registr = InterfaceReg()
        self.ui.pushButton.clicked.connect(self.auth)

        self.ui.pushButton_2.clicked.connect(self.open)

        self.base_line_edit = [self.ui.lineEdit_6, self.ui.lineEdit_7]

        self.check_db = CheckThread()
        self.check_db.mysignal.connect(self.signal_handler)

# проверка правильности ввода

    def open(self):
        self.registr.show()
    def check_input(funct):
        def wrapper(self):
            for line_edit in self.base_line_edit:
                if len(line_edit.text()) == 0:
                    return
            funct(self)
        return wrapper

# обработчик сигналов
    def signal_handler(self, value):
        print(value)
        QtWidgets.QMessageBox.about(self, 'Оповещение', value)
        name = self.ui.lineEdit_6.text()
        if value == "Успешно!":
            self.ui.login.setText("Добро пожаловать " + name)
            self.im.show()
            self.close()

    @check_input
    def auth(self):
        name = self.ui.lineEdit_6.text()
        passw = self.ui.lineEdit_7.text()
        self.check_db.thr_login(name, passw)


class InterfacePatient(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form3()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.reg)

        self.base_line_edit = [self.ui.lineEdit_6, self.ui.lineEdit_7,
                               self.ui.lineEdit_8, self.ui.lineEdit_9,
                               self.ui.lineEdit_10, self.ui.lineEdit_11,
                               self.ui.lineEdit_12]

        self.check_db = CheckThread()
        self.check_db.mysignal.connect(self.signal_handler)


    def reg(self):
        fio = self.ui.lineEdit_6.text()
        sex = self.ui.lineEdit_7.text()
        date = self.ui.lineEdit_8.text()
        address = self.ui.lineEdit_9.text()
        polis = self.ui.lineEdit_10.text()
        snils= self.ui.lineEdit_11.text()
        passport = self.ui.lineEdit_12.text()
        self.check_db.thr_patient(fio,sex,date,address,polis,snils,passport)

    def signal_handler(self, value):
        #self.ui.label.setText(name)
        QtWidgets.QMessageBox.about(self, 'Оповещение', value)

    def check_input(funct):
        def wrapper(self):
            for line_edit in self.base_line_edit:
                if len(line_edit.text()) == 0:
                    return
            funct(self)
        return wrapper


class InterfaceRaspis(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form111()
        self.ui.setupUi(self)
        self.recording = InterfaceRecording()

        self.ui.pushButton_2.clicked.connect(self.delraspis)
        self.ui.pushButton_3.clicked(self.open_recording)
        self.ui.pushButton_4.clicked.connect(self.closes)

        self.check_db = CheckThread()
        self.check_db.mysignal.connect(self.signal_handler)
        self.check_db.mysignal1.connect(self.signal_handler1)
    def closes(self):
        self.close()

    def open_recording(self):
        self.recording.show()
        self.recording.check()

    def signal_handler1(self, value):
        QtWidgets.QMessageBox.about(self, "Оповещение", value)

    def dbraspis(self):
        threading.Timer(10, self.dbraspis).start()
        if self.ui.checkBox.isChecked() == True:
            inf1 = self.ui.lineEdit.text()
        else:
            inf1 = "%"
        self.check_db.thr_dbraspis(inf1)

    def signal_handler(self, value):
        self.ui.tableWidget.setRowCount(len(value))
        for i, row in enumerate(value):
            item = QtWidgets.QTableWidgetItem()
            item.setData(Qt.EditRole, row[2])
            self.ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui.tableWidget.setItem(i, 2, item)
            self.ui.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.ui.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(row[4]))
            self.ui.tableWidget.resizeColumnsToContents()

    def delraspis(self):
        row = self.ui.tableWidget.currentItem().row()
        a = self.ui.tableWidget.item(row, 7).text()
        massage = QtWidgets.QMessageBox()
        value = massage.question(self, "Удаление", "Вы действительно хотите удалить запись ?",
                                   massage.Yes | massage.No)
        if value == massage.Yes:
            self.check_db.thr_delraspis(a,b)
        else:
            massage.close()
class InterfaceRecording(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form5()
        self.ui.setupUi(self)

        #self.ui.pushButton.clicked.connect(self.record)

        self.check_db = CheckThread()
        self.check_db.mysignal2.connect(self.signal_handler2)
        self.check_db.mysignal3.connect(self.signal_handler3)
        self.check_db.mysignal4.connect(self.signal_handler4)

    # def record(self):
    #     room=self.ui.lineEdit.text()
    #     patient=self.ui.lineEdit_2.text()
    #
    #     self.check_db.thr_recording(room,patient)

    def check(self):
        a=1
        self.check_db.thr_record(a)

    def signal_handler2(self, value):
        for i, row in enumerate(value):
            self.ui.comboBox_2.addItem(row[0])
    def signal_handler3(self, value):
        for i, row in enumerate(value):
            self.ui.comboBox_4.addItem(row[0])

    def signal_handler4(self, value):

        for i, row in enumerate(value):
            self.ui.comboBox_3.addItem(row[0])
class InterfaceRedpatient(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form7()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.redact)

        self.base_line_edit = [self.ui.lineEdit_6, self.ui.lineEdit_7,
                               self.ui.lineEdit_8, self.ui.lineEdit_9,]

        self.check_db = CheckThread()
        self.check_db.mysignal.connect(self.signal_handler)

    def redact(self):
        fio = self.ui.lineEdit_6.text()
        sex = self.ui.lineEdit_7.text()
        address = self.ui.lineEdit_8.text()
        passport = self.ui.lineEdit_9.text()
        self.check_db.thr_redpatient(fio,sex,address,passport)

    def signal_handler(self, value):
        QtWidgets.QMessageBox.about(self, 'Оповещение', value)

    def check_input(funct):
        def wrapper(self):
            for line_edit in self.base_line_edit:
                if len(line_edit.text()) == 0:
                    return
            funct(self)
        return wrapper


class InterfaceAccept(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form4()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.accept)

        self.base_line_edit = [self.ui.lineEdit, self.ui.lineEdit_2]
        self.base_text_edit = [self.ui.textEdit, self.ui.textEdit_2]

        self.check_db = CheckThread()
        self.check_db.mysignal.connect(self.signal_handler)

    def accept (self):
        sympt = self.ui.textEdit.text()
        cure = self.ui.textEdit_2.text()
        diagnos = self.ui.lineEdit.text()
        date = self.ui.lineEdit_2.text()
        self.check_db.thr_accept(sympt,cure,diagnos,date)

    def signal_handler(self, value):
        QtWidgets.QMessageBox.about(self, 'Оповещение', value)
    def check_input_text(funct):
        def wrapper(self):
            for text_edit in self.base_text_edit:
                if len(text_edit.text()) == 0:
                    return
            funct(self)
        return wrapper
    def check_input(funct):
        def wrapper(self):
            for line_edit in self.base_line_edit:
                if len(line_edit.text()) == 0:
                    return
            funct(self)
        return wrapper

class InterfaceRecipe(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form6()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.recipe)

        self.base_line_edit = [self.ui.lineEdit, self.ui.lineEdit_2,
                               self.ui.lineEdit_3, self.ui.lineEdit_4,
                               self.ui.lineEdit_5, self.ui.lineEdit_6]
        self.base_combo_box = [self.ui.comboBox]

        self.check_db = CheckThread()
        self.check_db.mysignal.connect(self.signal_handler)

    def recipe (self):
        for combo_box in self.base_combo_box:
            text = str(combo_box.currentText())
        if text == "Взрослый":
            combo = 1
        else:
            combo = 2
        type = combo
        fiop = self.ui.lineEdit.text()
        age = self.ui.lineEdit_2.text()
        fiod = self.ui.lineEdit_3.text()
        pill = self.ui.lineEdit_4.text()
        date = self.ui.lineEdit_5.text()
        life = self.ui.lineEdit_6.text()
        self.check_db.ththr_recipe(type,fiop,age,fiod,pill,date,life)

    def signal_handler(self, value):
        QtWidgets.QMessageBox.about(self, 'Оповещение', value)
    def check_input(funct):
        def wrapper(self):
            for line_edit in self.base_line_edit:
                if len(line_edit.text()) == 0:
                    return
            funct(self)
        return wrapper

class InterfaceRedwork(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form8()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.redwork)

        self.base_line_edit = [self.ui.lineEdit_6, self.ui.lineEdit_7, self.ui.lineEdit_8, self.ui.lineEdit_9,self.ui.lineEdit_10, self.ui.lineEdit_11, self.ui.lineEdit_12]

        self.check_db = CheckThread()
        self.check_db.mysignal.connect(self.signal_handler)

    def redwork(self):
        fio = self.ui.lineEdit_6.text()
        post = self.ui.lineEdit_7.text()
        address = self.ui.lineEdit_8.text()
        password = self.ui.lineEdit_9.text()
        money = self.ui.lineEdit_10.text()
        telefon = self.ui.lineEdit_11.text()
        date = self.ui.lineEdit_12.text()
        self.check_db.thr_redwork(fio, post, address, passport, money,telefon,date)

    def signal_handler(self, value):
        QtWidgets.QMessageBox.about(self, 'Оповещение', value)

    def check_input(funct):
        def wrapper(self):
            for line_edit in self.base_line_edit:
                if len(line_edit.text()) == 0:
                    return
            funct(self)
        return wrapper

class InterfaceWorker(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form11()
        self.ui.setupUi(self)

        self.ui.pushButton_2.clicked.connect(self.delworker)

        self.check_db = CheckThread()
        self.check_db.mysignal.connect(self.signal_handler)
        self.check_db.mysignal1.connect(self.signal_handler1)

    def closes(self):
        self.close()

    def dbworker(self):
        threading.Timer(10, self.dbworker).start()
        if self.ui.checkBox.isChecked() == True:
            inf1 = self.ui.lineEdit.text()
        else:
            inf1 = "%"
        self.check_db.thr_dbworker(inf1)

    def signal_handler(self, value):
        self.ui.tableWidget.setRowCount(len(value))
        for i, row in enumerate(value):
            item = QtWidgets.QTableWidgetItem()
            item.setData(Qt.EditRole, row[2])
            self.ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui.tableWidget.setItem(i, 2, item)
            self.ui.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.ui.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(row[4]))
            self.ui.tableWidget.setItem(i, 5, QtWidgets.QTableWidgetItem(row[5]))
            self.ui.tableWidget.setItem(i, 6, QtWidgets.QTableWidgetItem(row[6]))
            self.ui.tableWidget.setItem(i, 7, QtWidgets.QTableWidgetItem(row[7]))
            self.ui.tableWidget.resizeColumnsToContents()

    def delworker(self):
        row = self.ui.tableWidget.currentItem().row()
        a = self.ui.tableWidget.item(row, 7).text()
        massage = QtWidgets.QMessageBox()
        value = massage.question(self, "Удаление", "Вы действительно хотите удалить работника " + a + "?",
                                   massage.Yes | massage.No)
        if value == massage.Yes:
            self.check_db.thr_delworker(a)
        else:
            massage.close()

    def signal_handler1(self, value):
        QtWidgets.QMessageBox.about(self, "Оповещение", value)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mywin = InterfaceAuth()
    mywin.show()
    sys.exit(app.exec_())