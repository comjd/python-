"""
    定义函数，在列表中返回所有的偶数
"""


def mylist(old_list):
    index = 0
    while index < len(old_list):
        if old_list[index] % 2 == 0:
            yield old_list[index]
        index += 1


list01 = [89, 45, 2342, 34356, 343, 56, 6, 8, 745, 3]
for item in mylist(list01):
    print(item)
