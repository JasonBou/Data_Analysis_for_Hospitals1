import pandas as pd

df = pd.read_csv('/Users/jb/PycharmProjects/Data Analysis for Hospitals1/Topics/Working with missing values/Drop NaNs/data/dataset/input.txt')

df_nona = df.dropna(axis=0)
print(f'{df.shape[0]} {df_nona.shape[0]}')
#print(df.shape[0])
#print(df_nona.shape[0])

#  write your code here

