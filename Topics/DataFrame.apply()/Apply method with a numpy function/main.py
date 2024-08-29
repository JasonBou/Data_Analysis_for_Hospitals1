import pandas as pd
import numpy as np

def solution(df):
    df['sqrt'] = df.loc[:,'1'].apply(np.sqrt)
    print(df)
