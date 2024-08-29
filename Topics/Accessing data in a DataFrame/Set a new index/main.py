# your code here, the dataset is already loaded. The variable name is df_rock.

df_rock.index = ['EAO2', 'PD38', 'JL46', 'M7V9', 'PIYW']
df_rock.set_index('name', inplace=True)
print(df_rock.index)
