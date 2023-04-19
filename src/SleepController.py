import datetime
import sqlite3
from os import path
import Sleep as Sleep

class SleepController:
    def __init__(self) -> None:
        self.abspath = path.dirname(path.abspath(__file__))
        self.dbpath = path.join(self.abspath,"../database.db")
        self.create_table()
    
    def create_table(self):
        sql = sqlite3.connect(self.dbpath)
        cursor = sql.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS sleep (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            waktu_tidur DATETIME, 
            waktu_bangun DATETIME, 
            waktu_edit DATETIME)''')
        sql.commit()
        sql.close()

    def insert_sleep(self, waktu_tidur : datetime.datetime, waktu_bangun : datetime.datetime):
        sql = sqlite3.connect(self.dbpath)
        cursor = sql.cursor()
        newSleep = Sleep.Sleep(None, waktu_tidur, waktu_bangun)
        newSleep.insert_to_database(cursor)
        sql.commit()
        sql.close()
        
    def get_sleep_all(self):
        sql = sqlite3.connect(self.dbpath)
        cursor = sql.cursor()
        sleep_data = cursor.execute('''SELECT *
                                        FROM sleep
                                        GROUP BY waktu_tidur''').fetchall()
        sleep_data = [Sleep.Sleep(sleep[0], sleep[1], sleep[2], sleep[3]) for sleep in sleep_data]
        sql.close()
        return sleep_data

    def get_sleep_recent_duration(self):
        sleep_data = self.get_sleep_all()
        sleep_data = sleep_data[:7]
        duration_data = [((datetime.datetime.strptime(sleep.waktu_bangun, '%d/%m/%Y %H:%M:%S')
                         - datetime.datetime.strptime(sleep.waktu_tidur, '%d/%m/%Y %H:%M:%S')
                        ).total_seconds(), 
                          datetime.datetime.strptime(sleep.waktu_tidur, '%d/%m/%Y %H:%M:%S').strftime('%a')) 
                         for sleep in sleep_data]
        return duration_data
    
    def foreach(self, func):
        all_sleep = self.get_sleep_all()
        for x in all_sleep:
            func(x)