import pandas as pd
df = pd.read_csv('/Users/jb/PycharmProjects/Data Analysis for Hospitals1/Topics/Handling missing values/Handle missing values/data/dataset/input.txt')
df.dropna(axis=1, thresh=8 , inplace=True)
df = df.apply(lambda column: column.fillna(column.median()))
print(df.head(5))
