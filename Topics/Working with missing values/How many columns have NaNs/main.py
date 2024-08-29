import pandas as pd
df = pd.read_csv('/Users/jb/PycharmProjects/Data Analysis for Hospitals1/Topics/Working with missing values/How many columns have NaNs/data/dataset/input.txt')
print(df.isnull().any().sum())
#write your code here

