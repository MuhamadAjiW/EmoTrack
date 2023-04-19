import sqlite3
import datetime


class Mood:
    def __init__(self, mood=None, date=None):
        if date is None:
            date = datetime.datetime.now().strftime('%Y-%m-%d')

        self.mood = mood
        self.date = date

    def create_table(self, cursor: sqlite3.Cursor):
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS mood(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                mood TEXT,
                date DATE
            )
        """)

    def insert_to_database(self, cursor: sqlite3.Cursor):
        cursor.execute("""
            INSERT INTO mood(mood, date)
            VALUES('{0}', '{1}')
        """.format(self.mood, self.date))

    def update_from_database(self, cursor: sqlite3.Cursor):
        cursor.execute("""
            UPDATE mood
            SET mood = '{0}'
            WHERE date = '{1}'
        """.format(self.mood, self.date))

    def get_latest_date(self, cursor: sqlite3.Cursor):
        latestDate = cursor.execute("""
            SELECT date FROM mood
            ORDER BY date DESC
            LIMIT 1
        """).fetchone()
        if latestDate is None:
            return None
        return latestDate[0]

    def get_current_mood(self, cursor: sqlite3.Cursor):
        currentMood = cursor.execute("""
            SELECT mood FROM mood
            WHERE date = '{0}'
        """.format(self.date)).fetchone()
        if currentMood is None:
            return None
        return currentMood[0]

    def get_recent_moods(self, cursor: sqlite3.Cursor):
        return cursor.execute("""
            SELECT mood, date FROM mood
            ORDER BY date DESC
            LIMIT 30
        """).fetchall()
