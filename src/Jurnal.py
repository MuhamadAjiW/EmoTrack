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

    def createLabel(self):
        self.label = QtWidgets.QLabel()
        self.label.setObjectName("jurnal" + str(self.id))
        self.label.setText("{0} | {1}".format(self.waktuEdit, self.judul))
        self.label.mousePressEvent = self.show
        return self.label
    
    def show(self, event):
        from JurnalCreateForm import Ui_NewJurnalWindow
        self.ui = Ui_NewJurnalWindow(readOnly=True, jurnal=self)
        self.ui.show()
        pass

    def insert_to_database(self, cursor: sqlite3.Cursor):
        cursor.execute("""
            INSERT INTO jurnal(judul, isi, waktuEdit)
            VALUES('{}', '{}', '{}')
        """.format(self.judul, self.isi, self.waktuEdit))

def createFromTable(row):
    return Jurnal(row[0], row[1], row[2], row[3])