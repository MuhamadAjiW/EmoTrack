import datetime
import sqlite3
from PyQt5 import QtWidgets, QtCore

class Quote:
    def __init__(self, id, quote, waktuEdit = None, builtin = False):
        if waktuEdit is None:
            waktuEdit = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        self.id = id
        self.quote = quote
        self.waktuEdit = waktuEdit
        self.builtin = builtin

    def insert_to_database(self, cursor: sqlite3.Cursor):
        cursor.execute('INSERT INTO quotes (quote, date, builtin) VALUES (?, ?, ?)', (self.quote, self.waktuEdit, self.builtin))

def createFromTable(row):
    return Quote(row[0], row[1], row[2], row[3])