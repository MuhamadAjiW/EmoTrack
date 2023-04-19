import os
import sqlite3
import datetime

from Mood import Mood

dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))


class MoodController:
    def __init__(self):
        # Create database if it doesn't exist
        self.conn = sqlite3.connect(os.path.join(dir, "database.db"))
        self.cursor = self.conn.cursor()

        moodDB = Mood()
        moodDB.create_table(self.cursor)
        
        self.conn.commit()
        self.conn.close()

        self.updateMissingDates()

    def updateMissingDates(self):
        # Add missing dates to database
        self.conn = sqlite3.connect(os.path.join(dir, "database.db"))
        self.cursor = self.conn.cursor()

        moodDB = Mood()
        latestDate = moodDB.get_latest_date(self.cursor)
        
        if latestDate is None:
            return
        latestDatePlusOne = (datetime.datetime.strptime(
            latestDate, "%Y-%m-%d") + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        tommorow = (datetime.datetime.strptime(today, "%Y-%m-%d") +
                    datetime.timedelta(days=1)).strftime("%Y-%m-%d")

        while latestDatePlusOne != today and latestDatePlusOne != tommorow:
            newMood = Mood("NULL", latestDatePlusOne)
            newMood.insert_to_database(self.conn.cursor())
            self.conn.commit()
            latestDatePlusOne = (datetime.datetime.strptime(
                latestDatePlusOne, "%Y-%m-%d") + datetime.timedelta(days=1)).strftime("%Y-%m-%d")

        self.conn.close()

    def addMood(self, mood):
        # Add current mood to database
        currentMood = self.getCurrentMood()
        self.conn = sqlite3.connect(os.path.join(dir, "database.db"))
        self.cursor = self.conn.cursor()
        today = datetime.datetime.now().strftime("%Y-%m-%d")

        if currentMood is None:
            newMood = Mood(mood, today)
            newMood.insert_to_database(self.cursor)
        else:
            newMood = Mood(mood, today)
            newMood.update_from_database(self.cursor)
        self.conn.commit()
        self.conn.close()

    def getCurrentMood(self):
        # Get current mood
        self.conn = sqlite3.connect(os.path.join(dir, "database.db"))
        self.cursor = self.conn.cursor()

        moodDB = Mood()
        mood = moodDB.get_current_mood(self.cursor)
        
        self.conn.close()
        return mood

    def getRecentMoods(self):
        # Get last 30 days of moods
        self.conn = sqlite3.connect(os.path.join(dir, "database.db"))
        self.cursor = self.conn.cursor()

        moodDB = Mood()
        moods = moodDB.get_recent_moods(self.cursor)
        
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
