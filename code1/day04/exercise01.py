"""
    二分法查找
"""
import random


def search(old_list, value):

    low, high = 0, len(old_list) - 1
    print(old_list, value)
    while low <= high:
        mind = (low + high) // 2
        if old_list[mind] > value:
            high = mind - 1
        elif old_list[mind] < value:
            low = mind + 1
        else:
            return mind


if __name__ == '__main__':
    print(search([i for i in range(1,11)], random.randint(-5, 20)))