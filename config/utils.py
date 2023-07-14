import pandas as pd

def getDataFrame(url):
    df = pd.read_csv(url)
    return df