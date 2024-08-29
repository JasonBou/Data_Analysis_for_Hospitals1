#  write your code here 

import pandas as pd

df = pd.read_csv('/Users/jb/PycharmProjects/Data Analysis for Hospitals1/Topics/Handling missing values/Replace with the mode/data/dataset/input.txt')
mode_district = df['location'].mode()[0] # calculate the mode
df['location'].fillna(mode_district, inplace=True)
print(df.head(5))