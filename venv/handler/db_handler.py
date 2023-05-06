import pymysql
from check_db import *
from main import *
from main2 import *
from loginn import *
from patient import *
from regisration import *
from  mainform import *
from patient import *
from accept import *
from recording import *
from recipe import *
from redact_patient import *
from redact_worker import *
from nonee import *
from worker import *

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from config import host, user, password, db_name

try:
    connection = pymysql.Connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.Cursor
    )
    print("successfully connected...")

    def login(name, passw, signal):
        cursor = connection.cursor()

        value = cursor.execute(f'SELECT * FROM работники WHERE Логин="{name}" AND Пароль="{passw}";')
        if value > 0:
            signal.emit('Успешно!')
        else:
            signal.emit('Проверьте правильность ввода данных!')

    def register(fio, post, name, passw, role, signal):
        cursor = connection.cursor()

        value = cursor.execute(f'SELECT * FROM работники WHERE Логин="{name}";')
        if value > 0:
            signal.emit('Такой логин уже используется!')
        else:
            cursor.execute(f"INSERT INTO работники (ФИО, Должность, Логин, Пароль, Роль) VALUES ('{fio}','{post}', '{name}' , '{passw}', '{role}')")
            signal.emit('Вы успешно зарегистрированы!')
            connection.commit()
    def new_patient(fio,sex,date,address,polis,snils,passport, signal):
        cursor = connection.cursor()

        value = cursor.execute(f'SELECT * FROM пациент WHERE ПОЛИС="{polis}";')
        if value > 0:
            signal.emit('Такой пациент уже есть в базе!')
        else:
            cursor.execute(f"INSERT INTO пациент (ФИО,Пол, Дата_рождения, Адрес_прописки, ПОЛИС, СНИЛС, Паспорт) VALUES ('{fio}','{sex}', '{date}' , '{address}', '{polis}','{snils}', '{passport}')")
            signal.emit('Пациент успешно зарегистрирован!')
            connection.commit()
    def accept(sympt,cure,diagnos,date,signal):
        cursor = connection.cursor()

        value = cursor.execute(f'SELECT * FROM приём;')
        if value < 0:
            cursor.execute(f"INSERT INTO приём (Жалобы,Лечение, Диагноз, Дата_приёма) VALUES ('{sympt}','{cure}', '{diagnos}' , '{date}')")
            connection.commit()

    def redpatient(fio,sex,address,passport,signal):
        cursor = connection.cursor()

        value = cursor.execute(f'SELECT * FROM пациент ;')
        if value < 0:
            cursor.execute(
                f"INSERT INTO пациент (ФИО,Пол,Адрес_прописки, Паспорт) VALUES ('{fio}','{sex}',  '{address}', '{passport}')")
            connection.commit()

    def recipe(type,fiop,age,fiod,pill,date,life,signal):
        cursor = connection.cursor()
        value = cursor.execute(f'SELECT * FROM рецепты ;')
        if value < 0:
            cursor.execute(
                f"INSERT INTO пациент (Тип_рецепта,ФИО_пациента,Возраст,ФИО_врача, Лекарства,Дата_выдачи,Срок_годности_рецепта) VALUES ('{type}','{fiop}', '{age}', '{fiod}' ,'{pill}', '{date}','{life}')")
            connection.commit()

    def redwork(fio, post, address, passport, money,telefon,date,signal):
        cursor = connection.cursor()

        value = cursor.execute(f'SELECT * FROM работники ;')
        if value < 0:
            cursor.execute(
                f"INSERT INTO работники (ФИО,Должность,Адрес, Паспорт,Зарплата,Номер_телефона,Дата_рождения) VALUES ('{fio}','{post}',  '{address}', '{passport}','{money}','{telefon}','{date}')")
            connection.commit()

    def recording(room,patient,signal):
        cursor = connection.cursor()

        value = cursor.execute(f'SELECT * FROM расписание')
        if value < 0:
            cursor.execute(
                f"INSERT INTO расписание (Кабинет,Пациент) VALUES ('{room}','{patient}');")
            connection.commit()
    def record(a,signal2,signal3,signal4):
        cursor=connection.cursor()

        cursor.execute(f"SELECT Логин FROM работники")
        fio= cursor.fetchall()
        signal2.emit(fio)

        cursor.execute(f"SELECT Дата_приёма FROM приём")
        date = cursor.fetchall()
        signal3.emit(date)

        cursor.execute(f"SELECT Время_приёма FROM приём ")
        time = cursor.fetchall()
        signal4.emit(time)

    def dbworker(inf1, signal):
        cursor = connection.cursor()

        cursor.execute(f'SELECT ФИО, Должность, Зарплата, Адрес, Номер_телефона, Дата_рождения, Роль, Логин FROM работники '
                       f'WHERE ФИО LIKE "{inf1}"')
        inf = cursor.fetchall()

        signal.emit(inf)

    def delworker(a, signal):
        cursor = connection.cursor()

        cursor.execute(f'DELETE FROM работники WHERE Логин = "{a}"')
        signal.emit("Успешно")
        connection.commit()

    def delraspis(a,b, signal):
        cursor = connection.cursor()

        cursor.execute(f'DELETE FROM приём WHERE Дата_приёма = "{a}" AND Время_приёма="{b}"')
        signal.emit("Успешно")
        connection.commit()

    def dbraspis(inf1, signal):
        cursor = connection.cursor()

        cursor.execute(f'SELECT ФИО  FROM работники '
                       f'WHERE ФИО LIKE "{inf1}"')
        inf = cursor.fetchall()

        cursor.execute(f'SELECT Дата_приёма , Время_приёма  FROM приём')
        inf = cursor.fetchall()

        signal.emit(inf)

except Exception as ex:
        print("Connection refused...")
        print(ex)