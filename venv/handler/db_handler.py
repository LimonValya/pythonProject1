import pymysql
from main import *
from main2 import *
from loginn import *
from regisration import *
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
        cursorclass=pymysql.cursors.DictCursor
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


except Exception as ex:
        print("Connection refused...")
        print(ex)