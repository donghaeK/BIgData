import numpy as np
a1 = np.arange(1,6)
print(a1)
a2 = np.array([6,7,8,9,10])
a3 = np.array([
    [3,2,1],
    [-11,9,0]
])
print(a2)
print(a1+a2)
print(a1-a2)
print(a1 * a2)
print(np.dot(a1,a2))
# a3 = a1 + a2
# print(a3)
print(a1/a2)
print(np.sum(a1), np.sum(a2))
print(np.prod(a1), np.prod(a2))
print(a3.sum(axis=1))
print(a3.prod(axis=0))
print(a3.mean())
print(a3.std())