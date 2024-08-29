import pandas as pd
df = pd.read_csv('/Users/jb/PycharmProjects/Data Analysis for Hospitals1/Topics/Working with missing values/Proportions of NaNs/data/dataset/input.txt')
df_2 = df.isnull().sum() / df.shape[0]
print(df_2.round(decimals=2))
#  write your code here

