import datetime
import sqlite3
import Quote as Quote
from os import path
from random import randint

class QuoteController:
    def __init__(self):
        self.abspath = path.dirname(path.abspath(__file__))

        conn = sqlite3.connect(path.join(self.abspath, '../database.db'))
        conn.execute('CREATE TABLE IF NOT EXISTS quotes (id INTEGER PRIMARY KEY AUTOINCREMENT, quote TEXT, date TEXT, builtin BOOLEAN)')
        conn.commit()

        self.daftarQuotes = []

        cursor = conn.cursor()
        cursor.execute('SELECT * FROM quotes')
        entries = cursor.fetchall()
        for entry in entries:
            self.daftarQuotes += [Quote.createFromTable(entry)]

        conn.close()
    
    def foreach(self, func):
        for x in self.daftarQuotes:
            func(x)

    def addQuote(self, quote, waktuEdit = None, builtin = False):
        conn = sqlite3.connect(path.join(self.abspath, "../database.db"))
        newQuote = Quote.Quote(None, quote, waktuEdit, builtin)
        newQuote.insert_to_database(conn.cursor())
        self.daftarQuotes.append(newQuote)
        conn.commit()
        conn.close()

    def editQuote(self, idx, quote, waktuEdit = None, builtin = False):
        conn = sqlite3.connect(path.join(self.abspath, '../database.db'))
        cursor = conn.execute('SELECT * FROM quotes')
        rows = cursor.fetchall()
        id = rows[idx][0]

        if(waktuEdit == None):
            waktuEdit = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        conn.execute('UPDATE quotes SET quote = ?, date = ? WHERE id = ?', (quote, waktuEdit , id))
        conn.commit()

        self.daftarQuotes[idx].quote = quote

    def deleteQuote(self, idx):
        conn = sqlite3.connect(path.join(self.abspath, '../database.db'))
        cursor = conn.execute('SELECT * FROM quotes')
        rows = cursor.fetchall()
        id = rows[idx][0]
        conn.execute('DELETE FROM quotes WHERE id = ?', (id,))
        del(self.daftarQuotes[idx])
        conn.commit()
        conn.close()

    def fetchRandom(self):
        if len(self.daftarQuotes) == 0:
            return "Belum tersedia quote"
        random = randint(0, len(self.daftarQuotes) - 1)
        return self.daftarQuotes[random].quote

    def clearDB(self):
        conn = sqlite3.connect(path.join(self.abspath, '../database.db'))
        conn.execute('DELETE FROM quotes')
        conn.commit()
        conn.close()
