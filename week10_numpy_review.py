import numpy as np
# a1 = np.array([
#     [1,1,2],
#     [1,1,2],
#     [1,1,2]
# ])
# a2 = np.array([
#     [1,0,0],
#     [2,0,0],
#     [1,0,0]
# ])
a1 = np.ones((3,3))
a1[:, 2] =2
print(a1)


a2 = np.full((3,3), 5)
print(a2)

a3 = np.eye(3) #단일 행렬
print(a3)
#print(np.matmul(a1,a2))