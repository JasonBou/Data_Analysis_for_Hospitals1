#  write your code here 

import pandas as pd
df = pd.read_csv('/Users/jb/PycharmProjects/Data Analysis for Hospitals1/Topics/Summarizing numeric columns/Rock or Mine/data/dataset/input.txt')
r_median =df.loc[df.labels == 'R','null_deg'].median(axis=0).round(3)
m_median =df.loc[df.labels == 'M','null_deg'].median(axis=0).round(3)
print(f'M = {m_median} R = {r_median}')
