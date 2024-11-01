import polars as pl
import datetime as dt
import kagglehub
import random
import time
import pandas as pd
from sklearn.linear_model import LogisticRegression


# Extract
def make_data():
    # [5.1 3.5 1.4 0.2]
    rand = 4 + random.random()
    rand2 = 3 + random.random()
    rand3 = 1 + random.random()
    rand4 = random.random()
    # sepal_length,sepal_width,petal_length,petal_width
    di = {"sepal_length": rand, "sepal_width" : rand2, "petal_length" : rand3, "petal_width" : rand4}    
    
    return di

def polars_with_ml():

    # model
    temp = pl.read_csv("data/IRIS.csv")
    
    X = temp.drop('species')
    y = temp['species']
    
    clf = LogisticRegression(random_state=0).fit(X, y)

    start = time.time()

    result = []
    for i in range(0, 10):
        di = make_data()
        df = pl.DataFrame(di)
        di.update({"predict" : clf.predict(df)})
        result.append(di)
    
    print(f"polars :::: {time.time()-start:.4f} sec")
    # polars :::: 0.0023 sec


def pandas_with_ml():
    # model
    temp = pd.read_csv("data/IRIS.csv")

    X = temp.drop(columns='species')
    y = temp['species']
    
    clf = LogisticRegression(random_state=0).fit(X, y)

    start = time.time()

    result = []
    for i in range(0, 10):

        di = make_data()
        df = pd.DataFrame([di])
        di.update({"predict" : clf.predict(df)})
        result.append(di)

    print(f"pandas :::: {time.time()-start:.4f} sec")
    # pandas :::: 0.0049 sec

if __name__ == "__main__":
    polars_with_ml()
    pandas_with_ml()