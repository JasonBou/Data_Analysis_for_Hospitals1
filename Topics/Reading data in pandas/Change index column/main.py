#  write your code here
import pandas as pd

df = pd.read_csv('/Users/jb/PycharmProjects/Data Analysis for Hospitals1/Topics/Reading data in pandas/Change index column/data/dataset/name.txt',index_col='Name')
print(df.head(n=10))
