#  write your code here 
import pandas as pd
df_cars = pd.read_csv('/Users/jb/Downloads/hyperskill-dataset-100646336 (1).txt', sep=',')
df_cars.dropna(inplace=True)
df_cars ['Age'] =  df_cars['Age'].astype(int)
print (df_cars ['Age'].max())
#print(df_cars.describe())
#print(df_cars.describe(max()))
#print(df_cars.describe())