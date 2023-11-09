import pandas as pd
#dictionary
df1 = pd.DataFrame(
    {
        "KOR": [99,91,100],
        "ENG": [89,98,97],
        "MAT": [100,98,85]
    }, index=[1,2,3]
)
#print(df1)
#list
df2 = pd.DataFrame(
    [
        [99,89,100],
        [91,98,98],
        [100,97,85]
    ], index=[1,2,3],
    columns=["KOR","ENG","MAT"]
)
#print(df2)
print(df2)
# df2 = pd.melt(df2)
# print(df2)
df2 = pd.melt(df2).rename(columns={
    'variable' : 'subject',
    'value' : 'score'}).query('score >= 90')
print(df2)
