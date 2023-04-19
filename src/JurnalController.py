import sqlite3
from os import path
import Jurnal as Jurnal
import datetime

class JurnalController:
    def __init__(self) -> None:
        self.abspath = path.dirname(path.abspath(__file__))

        self.conn = sqlite3.connect(path.join(self.abspath,"database.db"))
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
        self.daftarJurnal = []
        for row in rows:
            self.daftarJurnal += [Jurnal.createFromTable(row)]

        self.conn.close()

    def foreach(self, func):
        for x in self.daftarJurnal:
            func(x)

    def checkToday(self):
        self.conn = sqlite3.connect(path.join(self.abspath,"database.db"))
        self.cursor = self.conn.cursor()
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        self.cursor.execute("""
            SELECT * FROM jurnal
            WHERE date(waktuEdit) = date('{0}')
        """.format(now))

        if len(self.cursor.fetchall()) > 0:
            raise Exception("Anda telah menulis jurnal hari ini.")

        self.conn.close()

    def getFrequencyArray(self, year):
        self.conn = sqlite3.connect(path.join(self.abspath,"database.db"))
        self.cursor = self.conn.cursor()
        
        self.cursor.execute("""
            SELECT COUNT(id), strftime('%m', waktuEdit) FROM jurnal
            WHERE strftime('%Y', waktuEdit) = '{0}'
            GROUP BY strftime('%m', waktuEdit)
            ORDER BY strftime('%m', waktuEdit)
        """.format(year))

        res = self.cursor.fetchall()
        self.conn.close()

        freq = [0 for i in range(12)]
        for i in range(12):
            for x in res:
                if i+1 == int(x[1]):
                    freq[i] = x[0]

        return freq
        
    def addJurnal(self, judul, isi, waktuEdit = None):
        newJurnal = Jurnal.Jurnal(None, judul, isi, waktuEdit)
        self.conn = sqlite3.connect(path.join(self.abspath,"database.db"))
        newJurnal.insert_to_database(self.conn.cursor())
        self.daftarJurnal.append(newJurnal)
        self.conn.commit()
        self.conn.close()

    def clearDB(self):
        conn = sqlite3.connect(path.join(self.abspath, 'database.db'))
        conn.execute('DELETE FROM quotes')
        conn.commit()
        conn.close()
        

if __name__ == '__main__':
    x = JurnalController()


