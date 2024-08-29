def solution(df):
    df = df.apply(min, result_type='broadcast')
    print(df)


