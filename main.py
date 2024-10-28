import polars as pl
import datetime as dt
import duckdb
import random
import time

# Extract
# 발생 시간, 이름, 금액 생성 method
def make_data():

    rand = random.randrange(0,4)
    rand2 = random.randrange(0,10)
    name_list = ["Alice Archer", "Ben Brown", "Chloe Cooper", "Daniel Donovan"]
    di = {  
            "date" : dt.datetime.now(),
            "name": name_list[rand],
            "amount": rand2 * 10000
        }
    return di

# Transfrom
def transform_data(n:int):
    """
    n : 데이터 몇개 생성할건지
    """
    # polars
    for i in range(0, n): 
        # 
        df = pl.DataFrame(make_data())
        save_data(df)

def save_data(df: pl.DataFrame):
    duckdb.sql("INSERT INTO Test SELECT * FROM df")
    pass

def get_data():
    result = duckdb.sql("SELECT * FROM Test")
    return result

def create_table():
    df = pl.DataFrame(make_data())
    duckdb.sql("CREATE TABLE Test AS SELECT * FROM df")

if __name__ == "__main__":

    create_table()
    transform_data(10)
    print(get_data())