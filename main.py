import polars as pl
import datetime as dt
import pandas as pd
import duckdb
import random
import time

# Extract
# 발생 시간, 이름
def make_data():

    rand = random.randrange(0,4)
    name_list = ["Alice Archer", "Ben Brown", "Chloe Cooper", "Daniel Donovan"]
    di = {  
            "date" : dt.datetime.now(),
            "name": name_list[rand],
            "amount": rand * 10000
        }
    return di

li = []
for i in range(0, 10000000):
    li.append(make_data())

# 데이터 프레임 선언

start = time.time()
df = pl.DataFrame(li)
result = duckdb.sql("SELECT * FROM df").show()
print(result)
print(f"polars :::: {time.time()-start:.4f} sec")

start2 = time.time()
df = pd.DataFrame(li)
result = duckdb.sql("SELECT * FROM df").show()
print(result)
print(f"pandas :::: {time.time()-start2:.4f} sec")


