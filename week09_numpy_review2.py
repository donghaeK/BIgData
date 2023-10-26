import numpy as np
import pandas as pd
df = pd.DataFrame({
    'A' : [1, 2, np.nan, 4],
    'B' : [5, np.nan, 7, 8],
    'C' : [9, 10, 11, np.nan]
})

#1
#df.fillna(df.mean(), inplace=True)
#print(df)

#2
# for col in df.columns:
#     print(col)
#     df[col] = np.where(pd.isnull(df[col]), np.mean(df[col]), df[col])
# print(df)

#3
from sklearn.impute import SimpleImputer
i = SimpleImputer(strategy='mean')
df = pd.DataFrame(i.fit_transform(df),columns=df.columns)
print(df)