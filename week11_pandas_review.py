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
#'KOR', 'MAT' column 추출 KOR>=95
df_copy = df2.loc[df2['KOR'] >= 95, ['KOR', 'MAT']]
print(df_copy)
#1번학생의 100점을 뽑을때
print(df2.at[1,'MAT'])

print(df2.iat[0,2])

