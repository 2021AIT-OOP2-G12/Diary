from diaries.AbstractDiary import AbstractDiary

class NakayamaDiary(AbstractDiary):

    def get_date(self):
        return "2021-12-09"

    def get_summary(self):
        return "グループワーク初日だった。リーダ決めと初期設定などを行った。"

    def get_author(self):
        return "Nakayama"