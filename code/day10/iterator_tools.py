class IterableHelper:
    @staticmethod
    def find_all(list, func):
        """
            查找列表中符合条件的所有元素
        :param list: 可迭代的对象
        :param func: 需要满足的条件函数
        :return: 满足条件的所有对象
        """
        if not getattr(list, '__iter__', False):  # 判断是否为可迭代对象
            return None
        if not callable(func):  # 判断是否为函数
            return None
        for item in list:
            if func(item):
                yield item

    @staticmethod
    def get_max(list, func):
        """
            查找列表中最大元素
        :param list: 可迭代的对象
        :param func: 需要满足的条件函数
        :return: 满足条件的一个对象
        """
        if not getattr(list, '__iter__', False):  # 判断是否为可迭代对象
            return None
        if not callable(func):  # 判断是否为函数
            return None
        if not list:  # 判断列表是否为空
            return None
        max_item = list[0]
        for i in range(len(list) - 1):
            if func(max_item) < func(list[i]):
                max_item = list[i]
        return max_item

    @staticmethod
    def sum(list, func):
        """
            查找列表中元素求和
        :param list: 可迭代的对象
        :param func: 求和的函数
        :return: 最终结果
        """
        if not getattr(list, '__iter__', False):  # 判断是否为可迭代对象
            return None
        if not callable(func):  # 判断是否为函数
            return None
        if not list:  # 判断列表是否为空
            return None
        sum_result = 0
        for item in list:
            sum_result += func(item)
        return sum_result

    @staticmethod
    def get_max(list, func):
        """
            查找列表中最大元素
        :param list: 可迭代的对象
        :param func: 需要满足的条件函数
        :return: 满足条件的一个对象
        """
        if not getattr(list, '__iter__', False):  # 判断是否为可迭代对象
            return None
        if not callable(func):  # 判断是否为函数
            return None
        if not list:  # 判断列表是否为空
            return None
        max_item = list[0]
        for i in range(len(list) - 1):
            if func(max_item) < func(list[i]):
                max_item = list[i]
        return max_item

    @staticmethod
    def is_exist(list, func):
        """
            在列表中是否存在满足条件的元素
        :param list: 可迭代的对象
        :param func: 满足的条件函数
        :return: 最终结果
        """
        if not getattr(list, '__iter__', False):  # 判断是否为可迭代对象
            return None
        if not callable(func):  # 判断是否为函数
            return None
        if not list:  # 判断列表是否为空
            return None
        for item in list:
            if func(item):
                return True
        return False

    @staticmethod
    def min(list, func):
        """
            查找列表中最小元素
        :param list: 可迭代的对象
        :param func: 需要满足的条件函数
        :return: 满足条件的一个对象
        """
        if not getattr(list, '__iter__', False):  # 判断是否为可迭代对象
            return None
        if not callable(func):  # 判断是否为函数
            return None
        if not list:  # 判断列表是否为空
            return None
        min_item = list[0]
        for i in range(len(list) - 1):
            if func(min_item) > func(list[i]):
                min_item = list[i]
        return min_item
