import pandas as pd
df = pd.read_csv('/Users/jb/PycharmProjects/Data Analysis for Hospitals1/Topics/Handling missing values/Guess the meaningful replacement/data/dataset/input.txt')#
new_totsp = df['livingsp']+ df['nonlivingsp']# calculate the median value
df['totsp'].fillna(new_totsp, inplace=True)
print(int(df['totsp'].sum()))

#write your code here

