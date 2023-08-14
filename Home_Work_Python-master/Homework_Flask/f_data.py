import sqlite3
import time
import math
import re
from flask import url_for


class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_menu(self):
        sql = 'SELECT * FROM chip'
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except IOError:
            print("Ошибка чтения из БД")
        return []


    def get_chip(self):
        sql = 'SELECT * FROM chip'
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except IOError:
            print("Ошибка чтения из БД")
        return []

    def add_post(self, name, characteristic, price):
        try:
            self.__cur.execute("SELECT COUNT() as 'count' FROM chip'")
            res = self.__cur.fetchone()

            if res['count'] > 0:
                print("Статья с таким URL уже существует")
                return False

            self.__cur.execute("INSERT INTO chip VALUES(NULL, ?, ?, ?)", (name, characteristic, price))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка добавления статьи в БД " + str(e))
            return False
        return True
