from diaries.DiarySample import DiarySample
from diaries.YokoyamaDiary import YokoyamaDiary
from diaries.ToyoshimaDiary import ToyoshimaDiary
from diaries.SugisakaDiary import SugisakaDiary


# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
  DiarySample(),
  YokoyamaDiary(),
  ToyoshimaDiary(),
  SugisakaDiary(),
] 

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()