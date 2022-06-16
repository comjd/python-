"""
    定义计算器，并返回
"""
import random

count = 0


def get_call_counters():
    global count
    count += 1
    return count


for i in range(random.randint(1, 100)):
    get_call_counters()
print(count)
