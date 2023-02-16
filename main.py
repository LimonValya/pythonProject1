import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets
from config import host, user, password, db_name


try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    print("successfully connected...")
    print("#" * 20)

    try:
        # select all data from table
        with connection.cursor() as cursor:
            select_all_rows = "SELECT * FROM `работники`"
            cursor.execute(select_all_rows)
            # cursor.execute("SELECT * FROM `users`")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            print("#" * 20)

    finally:
        connection.close()

except Exception as ex:
    print("Connection refused...")
    print(ex)