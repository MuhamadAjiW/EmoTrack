from Mood import *


class TestMood:
    def test_mood_ctor(self):
        mood = Mood(':)', '2021-04-01')
        assert mood.mood == ':)'
        assert mood.date == '2021-04-01'
