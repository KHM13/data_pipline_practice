import polars as pl
import datetime as dt
import duckdb
import random
import time
import pandas as pd

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
    pass

def save_data(df: pl.DataFrame):
    duckdb.sql("INSERT INTO Test SELECT * FROM df")
    pass

def get_data():
    result = duckdb.sql("SELECT * FROM Test WHERE amount > 20000")
    return result

def create_table():
    #df = pl.DataFrame(make_data())
    df = pd.DataFrame([make_data()])
    
    duckdb.sql("CREATE TABLE Test AS SELECT * FROM df")

def main():

    start = time.time()
    create_table()

    # polars
    for i in range(0, 10): 
        
        #df = pl.DataFrame(make_data())
        df = pd.DataFrame([make_data()])
        save_data(df)
    
    data = get_data()
    print(data)
    print(f"pandas :::: {time.time()-start:.4f} sec")
    #print(f"polars :::: {time.time()-start:.4f} sec")

    """
    polars :::: 0.2539 sec
    pandas :::: 0.0084 sec
    
    duckdb 와 같이 쓰면 판다스가 더 빠름
    아마 duckdb 측에서 최적화를 한걸로 예상함
    """
if __name__ == "__main__":
    main()