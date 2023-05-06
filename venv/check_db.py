from PyQt5 import QtCore, QtGui, QtWidgets
from handler.db_handler import *


class CheckThread(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(object)
    mysignal1 = QtCore.pyqtSignal(object)
    mysignal2 = QtCore.pyqtSignal(object)
    mysignal3 = QtCore.pyqtSignal(object)
    mysignal4 = QtCore.pyqtSignal(object)
    def thr_login(self, name, passw):
        login(name, passw, self.mysignal)

    def thr_register(self, fio, post, name, passw, role):
        register(fio, post, name, passw, role, self.mysignal)

    def thr_main(self,name,passw):
        main(name,passw,self.mysignal)

    def thr_patient(self,fio,sex,date,address,polis,snils,passport):
        new_patient(fio,sex,date,address,polis,snils,passport,self.mysignal)

    def thr_accept(self,sympt,cure,diagnos,date):
        accept(sympt,cure,diagnos,date,self.mysignal)

    def thr_recording(self,room,patient):
        recording(room,patient,self.mysignal)

    def thr_record(self, a):
        record(a,self.mysignal2,self.mysignal3,self.mysignal4)

    def thr_redwork(self,fio, post, address, passport, money,telefon,date):
        redwork(fio, post, address, passport, money,telefon,date,self.mysignal)

    def thr_recipe(self,type,fiop,age,fiod,pill,date,life):
        recipe(type,fiop,age,fiod,pill,date,life,self.mysignal)

    def thr_redpatient(self,fio,sex,address,passport):
        redpatient(fio,sex,address,passport,self.mysignal)

    def thr_dbworker(self, inf1):
        dbworker(inf1, self.mysignal)

    def thr_delworker(self, a):
        delworker(a, self.mysignal1)

    def thr_delraspis(self,a,b):
        delraspis(a,b,self.mysignal1)

    def thr_dbraspis(self, inf1):
        dbworker(inf1, self.mysignal)