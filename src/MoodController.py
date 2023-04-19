import os
import sqlite3
import datetime

dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))


class MoodController:
    def __init__(self) -> None:
        # Create database if it doesn't exist
        self.conn = sqlite3.connect(os.path.join(dir, "database.db"))
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS mood(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                mood TEXT,
                date DATE
            );
        """)
        self.conn.commit()
        self.conn.close()

        self.updateMissingDates()

    def updateMissingDates(self):
        # Add missing dates to database
        self.conn = sqlite3.connect(os.path.join(dir, "database.db"))
        self.cursor = self.conn.cursor()

        latestDate = self.cursor.execute("""
                        SELECT date FROM mood
                        ORDER BY date DESC
                        LIMIT 1
                    """).fetchone()
        if latestDate is None:
            return
        latestDatePlusOne = (datetime.datetime.strptime(
            latestDate[0], "%Y-%m-%d") + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        tommorow = (datetime.datetime.strptime(today, "%Y-%m-%d") +
                    datetime.timedelta(days=1)).strftime("%Y-%m-%d")

        while latestDatePlusOne != today and latestDatePlusOne != tommorow:
            self.conn.execute("""
                INSERT INTO mood(mood, date)
                VALUES('NULL', '{0}')
            """.format(latestDatePlusOne))
            self.conn.commit()
            latestDatePlusOne = (datetime.datetime.strptime(
                latestDatePlusOne, "%Y-%m-%d") + datetime.timedelta(days=1)).strftime("%Y-%m-%d")

        self.conn.close()

    def addMood(self, mood):
        # Add current mood to database
        self.conn = sqlite3.connect(os.path.join(dir, "database.db"))
        self.cursor = self.conn.cursor()
        today = datetime.datetime.now().strftime("%Y-%m-%d")

        self.cursor.execute("""
            SELECT * FROM mood
            WHERE date = '{0}'
        """.format(today))

        if self.cursor.fetchone() is None:
            self.conn.execute("""
                INSERT INTO mood(mood, date)
                VALUES('{0}', '{1}')
            """.format(mood, today))
        else:
            self.conn.execute("""
                UPDATE mood
                SET mood = '{0}'
                WHERE date = '{1}'
            """.format(mood, today))
        self.conn.commit()
        self.conn.close()

    def getCurrentMood(self):
        # Get current mood
        self.conn = sqlite3.connect(os.path.join(dir, "database.db"))
        self.cursor = self.conn.cursor()
        today = datetime.datetime.now().strftime("%Y-%m-%d")

        self.cursor.execute("""
            SELECT mood FROM mood
            WHERE date = '{0}'
        """.format(today))
        mood = self.cursor.fetchone()
        self.conn.close()
        if mood is None:
            return "NULL"
        return mood[0]

    def getRecentMoods(self):
        # Get last 30 days of moods
        self.conn = sqlite3.connect(os.path.join(dir, "database.db"))
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
            SELECT mood, date FROM mood
            ORDER BY date DESC
            LIMIT 30
        """)
        moods = self.cursor.fetchall()
        self.conn.close()
        return moods

    def getPercentage(self, mood):
        # Get percentage of mood in last 30 days
        moods = self.getRecentMoods()
        totalMood = min(len(moods), 30)
        countMood = 0

        for m in moods:
            if m[0] == mood:
                countMood += 1

        if totalMood == 0:
            return 0
        return (int)(countMood / totalMood * 100)


if __name__ == '__main__':
    MoodController()
