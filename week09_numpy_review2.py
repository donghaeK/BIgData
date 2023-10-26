import numpy as np
data = np.array([
     [1, 5, 9],
     [2, np.nan, 10],
     [np.nan, 7, 11],
     [4, 8, np.nan]
])
print(data)

means= np.nanmean(data, axis=0)
print(means)

for i in range(data.shape[1]):
    mask = np.isnan(data[:, i]) #nan인부분 true / false로 구분
    data[mask, i] = means[i]
    print(data)