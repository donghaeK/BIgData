import numpy as np
from numpy.linalg import inv
#linalg == linear algebra -> 역행렬함수
import matplotlib.pyplot as plt
np.random.seed()
a = np.random.uniform(size=10000) #균등분포(일양분포)
print(a)
b = np.random.normal(0,1,1000) #정규분포
print(b)
plt.hist(a)
#plt.hist(b)
plt.show()
