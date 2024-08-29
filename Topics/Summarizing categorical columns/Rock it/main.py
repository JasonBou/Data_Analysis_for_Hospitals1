#  write your code here 

import pandas as pd

df = pd.read_csv('/Users/jb/PycharmProjects/Data Analysis for Hospitals1/Topics/Summarizing categorical columns/Rock it/data/dataset/input.txt')

print(df.labels.value_counts().loc['R'])
