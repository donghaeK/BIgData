import pandas as pd
df2 = pd.DataFrame(
    [
        [99,89,81],
        [91,98,98],
        [95,97,85],
        [83,96,94]
    ], index=[1,2,3,4],
    columns=["KOR", "ENG", "MAT"]
)
print(df2)
df2 = df2.apply(lambda n : n+1)
print(df2)