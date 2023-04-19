import datetime
import sqlite3
from PyQt5 import QtWidgets, QtCore

class Sleep:
    def __init__(self, id, waktu_tidur, waktu_bangun, waktuEdit = None):
        if waktuEdit is None:
            waktuEdit = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')

        self.id = id
        self.waktu_tidur = waktu_tidur
        self.waktu_bangun = waktu_bangun
        self.waktuEdit = waktuEdit

    def insert_to_database(self, cursor: sqlite3.Cursor):
        cursor.execute("""INSERT INTO sleep(waktu_tidur, waktu_bangun, waktu_edit) 
                    VALUES('{}', '{}', '{}')""".format( 
                    self.waktu_tidur, self.waktu_bangun, self.waktuEdit))

def createFromTable(row):
    return Sleep(row[0], row[1], row[2], row[3])