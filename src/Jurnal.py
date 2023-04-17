import datetime
import sqlite3
from PyQt5 import QtWidgets, QtCore

class Jurnal:
    def __init__(self, id, judul, isi, waktuEdit = None):
        if waktuEdit is None:
            waktuEdit = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        self.id = id
        self.judul = judul
        self.isi = isi
        self.waktuEdit = waktuEdit

    def createFromTable(self, row):
        self.id = row[0]
        self.judul = row[1]
        self.isi = row[2]
        self.waktuEdit = row[3]

    def createLabel(self, scrollArea):
        self.label = QtWidgets.QLabel(scrollArea)
        self.label.setObjectName("jurnal" + str(self.id))
        self.label.setText("{0} | {1}".format(self.waktuEdit, self.judul))
        return self.label

    def insert_to_database(self, cursor: sqlite3.Cursor):
        cursor.execute("""
            INSERT INTO jurnal
            VALUES(null, '%s', '%s', '%s')
        """.format(self.judul, self.isi, self.waktuEdit))
    