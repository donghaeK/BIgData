import pandas as pd
df2 = pd.DataFrame(
    [
        [99,89,100],
        [91,98,98],
        [100,97,85],
        [83,100,94]
    ], index=[1,2,3,4],
    columns=["KOR","ENG","MAT"]
)
print(df2)
df2_copy = df2.iloc[:,[0,2]]
print(df2_copy)

df3_copy = df2.loc[:,['KOR', 'MAT']]
print(df3_copy)

df4_copy = df2.loc[:,'KOR':'MAT']
print(df4_copy)

df2 = pd.melt(df2)\
    .rename(columns={
    'variable' : 'subject',
    'value' : 'score'})\
    .query('score >= 90')\
    .sort_values('score', ascending=False)
print(df2)

print(df2.iloc[:,[1]])



