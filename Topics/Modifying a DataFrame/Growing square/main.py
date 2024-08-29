import pandas as pd

df = pd.DataFrame({'a': [1, 4], 'b': [2, 5]})
new_row = {'a': 7,
            'b': 8}
df = pd.concat([df, pd.DataFrame.from_records([new_row])], ignore_index=True)
df['c'] = [3, 6, 9]
#print(df)
# Your code here