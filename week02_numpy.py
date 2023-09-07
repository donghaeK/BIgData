import numpy as np
import random

x = int(input("수를 입력하세요 : "))

l = [random.randint(1, 100) for i in range(x)]

v = np.array(l, dtype='int16')
print(v)





