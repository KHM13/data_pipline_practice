import polars as pl
import datetime as dt
import pandas as pd
import duckdb
import random
import time

# 발생 시간, 이름, 금액 생성 method
def make_data():

    rand = random.randrange(0,4)
    name_list = ["Alice Archer", "Ben Brown", "Chloe Cooper", "Daniel Donovan"]
    di = {  
            "date" : dt.datetime.now(),
            "name": name_list[rand],
            "amount": rand * 10000
        }
    return di

if __name__ == "__main__":

    start2 = time.time()

    for i in range(0, 10000):

        # pandas
        df2 = pd.DataFrame([make_data()])
        result = duckdb.sql("SELECT * FROM df2").show()
        #print(result)

    pt = time.time()-start2
    #print(f"pandas :::: {time.time()-start2:.4f} sec")


    # polars
    start = time.time()
    for i in range(0, 10000):

        df = pl.DataFrame(make_data())
        result = duckdb.sql("SELECT * FROM df").show()
        #print(result)

    print(f"polars :::: {time.time()-start:.4f} sec")
    print(f"pandas :::: {pt:.4f} sec")
    
    # 만건 기준
    # polars :::: 6.3179 sec
    # pandas :::: 7.0262 sec