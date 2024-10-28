import polars as pl
import datetime as dt
import pandas as pd
import random
import time

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

if __name__ == "__main__":



    # polars
    start = time.time()
    for i in range(0, 10000):
        df = pl.DataFrame(make_data())
        df.drop('amount')

    print(f"polars :::: {time.time()-start:.4f} sec")

    # pandas
    start2 = time.time()
    for i in range(0, 10000):
        df2 = pd.DataFrame([make_data()])
        df2.drop('amount', axis=True)

    pt = time.time()-start2
    print(f"pandas :::: {time.time()-start2:.4f} sec")
    
    """
    결론

    10000건 기준
    polars :::: 0.4949 sec
    pandas :::: 1.1726 sec
    보통 pandas 호출만 했을 뿐인데 TPS가 반토막 나는 이슈가 있는데 polars가 2배 빠름
    """