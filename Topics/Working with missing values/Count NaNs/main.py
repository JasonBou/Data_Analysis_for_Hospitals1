import pandas as pd

df = pd.read_csv('/Users/jb/PycharmProjects/Data Analysis for Hospitals1/Topics/Working with missing values/Count NaNs/data/dataset/input.txt')
print(df.isnull().sum())
#  write your code here

