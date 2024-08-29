def sum_row(row):
    return (row[0] + row[1]) / 10.5        

def solution(df):
    df = df.apply(sum_row,axis=1,result_type='reduce')
    print(df)