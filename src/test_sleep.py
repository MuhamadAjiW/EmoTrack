import pytest
from os import path
from SleepController import *
from Sleep import *

class TestSleep:
    def test_sleep_ctor(self):
        waktu_tidur = "19/4/2023 23:55:00"
        waktu_bangun = "20/4/2023 23:55:00"
        waktu_edit = "20/4/2023 23:55:00"
        sleep = Sleep(None, waktu_tidur, waktu_bangun)
        assert sleep.id is None
        assert sleep.waktuEdit is not None
        assert sleep.waktu_tidur == waktu_tidur
        assert sleep.waktu_bangun == waktu_bangun

    def test_curnal_ctor_from_table(self):
        waktu_tidur = "19/4/2023 23:55:00"
        waktu_bangun = "20/4/2023 23:55:00"
        waktu_edit = "20/4/2023 23:55:00"
        sleep = createFromTable([3, waktu_tidur, waktu_bangun, waktu_edit])
        assert sleep.id == 3
        assert sleep.waktuEdit == waktu_edit
        assert sleep.waktu_tidur == waktu_tidur
        assert sleep.waktu_bangun == waktu_bangun

    def test_fetch_all_not_null(self):
        controller = SleepController()
        def checkNull(sleep):
            assert sleep is not None
        controller.foreach(checkNull)
    
    def test_fetch_all_sleep(self):
        controller = SleepController()
        sleep_data = controller.get_sleep_all()
        
        abspath = path.dirname(path.abspath(__file__))
        dbpath = path.join(abspath,"../database.db")
        sql = sqlite3.connect(dbpath)
        cursor = sql.cursor()
        table_length = int(cursor.execute('''SELECT COUNT(*) FROM sleep''').fetchone()[0])
        assert len(sleep_data) == table_length
        
    def test_fetch_recent_sleep(self):
        controller = SleepController()
        recent_sleep = controller.get_sleep_recent_duration()
        assert len(recent_sleep) <= 7
