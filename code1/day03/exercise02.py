"""
    排序算法：快速排序、冒泡排序、选择排序、插入排序
"""
import random
import time


def sum01(start, end):
    s1 = time.time()
    result = 0
    for i in range(start, end + 1):
        result += i
    print(time.time() - s1)
    return result


def sum02(star, end):
    s1 = time.time()
    result = (star + end) * (end - star + 1) / 2
    print(time.time() - s1)
    return result


def print_time(func):
    # index = 0

    def wrap(*args, **kwargs):
        # s1 = time.time()
        # nonlocal index
        func(*args, **kwargs)
        # s2 = time.time()

    return wrap


class MyOrder:
    @print_time
    def quick(self, old_list, low=0, high=-2):
        """
            快速排序
        :param old_list: 待排序的列表
        :param low: 排序的开始位置
        :param high: 排序的结束位置
        """
        if high == -2:
            high = len(old_list) - 1
        if low < high:
            index = MyOrder.__sub_sort(old_list, low, high)
            self.quick(old_list, low, index - 1)
            self.quick(old_list, index + 1, high)

    @staticmethod
    def __sub_sort(old_list, low, high):
        temp = old_list[low]
        while low < high:
            while old_list[high] >= temp and high > low:
                high -= 1
            old_list[low] = old_list[high]
            while old_list[low] < temp and low < high:
                low += 1
            old_list[high] = old_list[low]
        old_list[low] = temp
        return low

    @staticmethod
    def bubble(old_list, asc=True):
        """
            冒泡排序
        :param old_list:待排序的列表
        :param asc:True顺序,False倒序
        """
        for i in range(len(old_list) - 1):
            for j in range(len(old_list) - 1 - i):
                if asc:
                    if old_list[j] >= old_list[j + 1]:
                        old_list[j], old_list[j + 1] = old_list[j + 1], old_list[j]
                else:
                    if old_list[j] < old_list[j + 1]:
                        old_list[j], old_list[j + 1] = old_list[j + 1], old_list[j]

    @staticmethod
    def select(old_list, asc=True):
        """
            选择排序
        :param old_list: 待排序的列表
        :param asc: True顺序,False倒序
        :return:
        """
        for i in range(len(old_list) - 1):
            temp = i
            for j in range(i + 1, len(old_list)):
                if asc:  # 顺序
                    if old_list[j] < old_list[temp]:
                        temp = j
                else:  # 倒序
                    if old_list[j] >= old_list[temp]:
                        temp = j
            if temp != i:
                old_list[i], old_list[temp] = old_list[temp], old_list[i]

    @staticmethod
    def insert(old_list, asc=True):
        """
            插入排序
        :param old_list: 待排序的列表
        :param asc: True顺序,False倒序
        :return:
        """
        for i in range(1, len(old_list)):
            temp = old_list[i]
            j = i - 1
            if asc:
                while j >= 0 and old_list[j] > temp:
                    old_list[j + 1] = old_list[j]
                    j -= 1
            else:
                while j >= 0 and old_list[j] <= temp:
                    old_list[j + 1] = old_list[j]
                    j -= 1

            old_list[j + 1] = temp


if __name__ == '__main__':
    # ord = MyOrder()
    # l = [random.randint(1, 100) for i in range(8)]
    # print(l)
    # ord.quick(l)
    # print(l)
    # l = [random.randint(1, 1000) for i in range(10)]
    # print(l)
    # MyOrder.bubble(l, False)
    # print(l)
    # l = [random.randint(1, 100) for i in range(10)]
    # print(l)
    # MyOrder.select(l, False)
    # print(l)
    l = [random.randint(1, 100) for i in range(10)]
    print(l)
    MyOrder.insert(l, False)
    print(l)
