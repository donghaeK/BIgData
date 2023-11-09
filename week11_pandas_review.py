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
#영어,국어성적이 95

print(df2.query('KOR>=95 and ENG>=95'))
