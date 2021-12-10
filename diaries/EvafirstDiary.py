from diaries.AbstractDiary import AbstractDiary

class EvafirstDiary(AbstractDiary):

    def get_date(self):
        return "2021-12-09"

    def get_summary(self):
        return "グループ作業初日"

    def get_author(self):
        return "Evafirst"