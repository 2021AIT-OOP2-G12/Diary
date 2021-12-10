from diaries.AbstractDiary import AbstractDiary

class ToyoshimaDiary(AbstractDiary):
    def get_date(self):
        return "2021-12-09"
    def get_summary(self):
        return "今日はグループワーク初日だった。"
    def get_author(self):
        return "Toyoshima"