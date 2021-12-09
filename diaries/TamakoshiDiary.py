from diaries.AbstractDiary import AbstractDiary

class TamakoshiDiary(AbstractDiary):

    def get_date(self):
        return "2021-12-09"

    def get_summary(self):
        return "グループワーク初日緊張した。"

    def get_author(self):
        return "Tamakoshi"