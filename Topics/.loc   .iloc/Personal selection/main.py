# your code here. The data frame is already loaded and stored as chart2020.

import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv')
print(df.flipper_length_mm.mean())
print(df.flipper_length_mm.median())
print(df.sex.mode())
print(df.nunique())