"""
    随机产生2个数字(1--10)的加法

"""

import random

socre = 0
for i in range(3):
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    r = int(input(('%d+%d=' % (x, y))))
    if r == x + y:
        socre += 10
    else:
        socre -= 5
print(socre)
