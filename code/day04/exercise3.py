"""
    列表推导式
    将1-10的数字的平方，存入list01
    然后将list01奇数存入list02
    然后将list01大于5的偶数+1存入list03
"""

list01 = [i ** 2 for i in range(1, 11)]
print(list01)

list02 = [i for i in list01 if i % 2 == 1]
print(list02)

list03 = [i + 1 for i in list01 if i > 5 and i % 2 == 0]
print(list03)
