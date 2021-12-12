from diaries.DiarySample import DiarySample
from diaries.YokoyamaDiary import YokoyamaDiary
from diaries.ToyoshimaDiary import ToyoshimaDiary
from diaries.TamakoshiDiary import TamakoshiDiary
from diaries.SugisakaDiary import SugisakaDiary
from diaries.EvafirstDiary import EvafirstDiary
from diaries.NakayamaDiary import NakayamaDiary
from diaries.TakakiDiary import TakakiDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
  DiarySample(),
  YokoyamaDiary(),
  ToyoshimaDiary(),
  TamakoshiDiary(),
  SugisakaDiary(),
  EvafirstDiary(),
  NakayamaDiary(),
  TakakiDiary()
] 

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()