from diaries.DiarySample import DiarySample
<<<<<<< HEAD
from diaries.TamakoshiDiary import TamakoshiDiary
=======
from diaries.YokoyamaDiary import YokoyamaDiary
from diaries.ToyoshimaDiary import ToyoshimaDiary
from diaries.TamakoshiDiary import TamakoshiDiary
from diaries.SugisakaDiary import SugisakaDiary
from diaries.EvafirstDiary import EvafirstDiary
from diaries.NakayamaDiary import NakayamaDiary
>>>>>>> 94fb2e5047d923be6eb97c9691d7bc63f4983be5

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
  DiarySample(),
<<<<<<< HEAD
  TamakoshiDiary()
]
=======
  YokoyamaDiary(),
  ToyoshimaDiary(),
  TamakoshiDiary(),
  SugisakaDiary(),
  EvafirstDiary(),
  NakayamaDiary()
] 
>>>>>>> 94fb2e5047d923be6eb97c9691d7bc63f4983be5

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()