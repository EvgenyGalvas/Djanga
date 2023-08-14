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
        sql = 'SELECT * FROM mainmenu'
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except IOError:
            print('Ошибка чтения из БД')
        return []

    def add_book(self, title, text, url):
        try:
            self.__cur.execute("SELECT COUNT() as 'count' FROM books WHERE url LIKE ?", (url,))
            res = self.__cur.fetchone()
            if res['count'] > 0:
                print("Статья с таким URL уже существует")
                return False



            tm = math.floor(time.time())
            self.__cur.execute("INSERT INTO books VALUES(NULL, ?, ?, ?, ?)", (title, text, url, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print('Ошибка добавления книги в БД ' + str(e))
            return False
        return True

    def get_post(self, alias):
        try:
            self.__cur.execute(f"SELECT title, text FROM books WHERE url = '{alias}'")
            res = self.__cur.fetchone()
            if res:
                return res
        except sqlite3.Error as e:
            print('Ошибка получения книги из БД ' + str(e))
        return False, False

    def get_books_annonce(self):
        try:
            self.__cur.execute("SELECT id, title, text, url FROM books ORDER BY time DESC")
            res = self.__cur.fetchall()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения статей из БД " + str(e))
        return []

