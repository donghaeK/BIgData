import numpy as np
import random

x = int(input("수를 입력하세요 : "))
l = list()
for i in range(x):
    l.append(random.randint(1, 100))

    v = np.array(l, dtype='int16')
    print(v)


