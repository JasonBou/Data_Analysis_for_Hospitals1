#  write your code here 

import pandas as pd

df = pd.read_csv('/Users/jb/PycharmProjects/Data Analysis for Hospitals1/Topics/Reshaping and Pivot Tables/Mean/data/dataset/input.txt')
df_newpivot = df.pivot_table(index='labels',aggfunc='mean').round(2)
print(df_newpivot.loc['R','null_deg'])

