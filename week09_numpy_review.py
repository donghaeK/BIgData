import numpy as np

def info(x):
    print(f"배열의 차원은 {x.ndim}")
    print(f"원소의 개수는 {x.size}")
    print(f"배열의 shape는 {x.shape}")
np_1d = np.arange(1, 20, 2)
info(np_1d)

np_1d = np_1d.reshape(1, 2, 5)
print(np_1d)


