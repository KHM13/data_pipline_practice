import polars as pl
import datetime as dt
import duckdb
import random

# Extract
# 발생 시간, 이름
def make_data():

    rand = random.randrange(0,4)
    name_list = ["Alice Archer", "Ben Brown", "Chloe Cooper", "Daniel Donovan"]
    di = {  
            "date" : dt.datetime.now(),
            "name": name_list[rand]
        }
    return di


li = []
for i in range(0, 10000):
    li.append(make_data())

# 데이터 프레임 선언
df = pl.DataFrame(li)
print(df)

# transform




# load



