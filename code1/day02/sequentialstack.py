"""
    顺序栈
"""


class StackError(Exception):
    pass


class SequentialStack:
    def __init__(self):
        self.__stack = []

    @property
    def stack(self):
        return self.__stack

    def is_empty(self):
        """
            判断栈是否为空
        :return: True栈为空，False栈不为空
        """
        return self.__stack == []

    def push(self, value):
        """
            入栈
        :param value:
        """
        self.__stack.append(value)

    def pop(self):
        """
            出栈
        :return:出栈的元素
        """
        if self.is_empty():
            raise StackError('栈为空')
        return self.__stack.pop()

    def top(self):
        """
            获取栈顶的元素（最后一个）
        :return:
        """
        if self.is_empty():
            # raise StackError('栈为空')
            self.__print_info()
        else:
            return self.__stack[-1]

    def show(self):
        if self.is_empty():
            self.__print_info()
            return
        for element in self.__stack:
            print(element)

    def len(self):
        """
            获取元素个数
        :return: 元素个数
        """
        return len(self.__stack)

    def clear(self):
        """
            清空栈
        :return:
        """
        self.__stack = []

    @staticmethod
    def __print_info(is_print=1):
        if is_print == 1:
            print('stack empty')


if __name__ == '__main__':
    stack = SequentialStack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(stack.is_empty())
    stack.show()
    stack.pop()
    # stack.pop()
    stack.pop()
    stack.show()
