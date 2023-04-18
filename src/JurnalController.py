import sqlite3
import os
import Jurnal
import datetime

dir = os.path.dirname(os.path.realpath(__file__))

class JurnalController:
    def __init__(self) -> None:
        self.conn = sqlite3.connect(os.path.join(dir,"database.db"))
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS jurnal(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                judul VARCHAR(255) NOT NULL,
                isi MEDIUMTEXT,
                waktuEdit DATETIME
            );
        """)
        self.conn.commit()
        self.cursor.execute("""
            SELECT * FROM jurnal
        """)

        rows = self.cursor.fetchall()
        self.daftar_jurnal = []
        for row in rows:
            self.daftar_jurnal += [Jurnal.createFromTable(row)]

        self.conn.close()

    def foreach(self, func):
        for x in self.daftar_jurnal:
            func(x)

    def checkToday(self):
        self.conn = sqlite3.connect(os.path.join(dir,"database.db"))
        self.cursor = self.conn.cursor()
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        self.cursor.execute("""
            SELECT * FROM jurnal
            WHERE date(waktuEdit) = date('{0}')
        """.format(now))

        if len(self.cursor.fetchall()) > 0:
            raise Exception("Anda telah menulis jurnal hari ini.")
        
    def addJurnal(self, judul, isi, waktuEdit = None):
        newJurnal = Jurnal.Jurnal(None, judul, isi, waktuEdit)
        self.conn = sqlite3.connect(os.path.join(dir,"database.db"))
        newJurnal.insert_to_database(self.conn.cursor())
        self.daftar_jurnal.append(newJurnal)
        self.conn.commit()
        




if __name__ == '__main__':
    x = JurnalController()


