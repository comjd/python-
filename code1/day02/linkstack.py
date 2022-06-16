"""
    链式栈
"""


class StackError(Exception):
    pass


class LinkNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class LinkStack:
    def __init__(self):
        self.__top = None
        self.__temp = None

    @property
    def top(self):
        return self.__top

    def is_empty(self):
        """
            判断栈是否为空
        :return: True栈为空，False栈不为空
        """
        return self.__top is None

    def push(self, value):
        """
            入栈
        :param value:
        """
        self.__top = LinkNode(value, self.__top)

    def pop(self):
        """
            出栈
        :return:出栈的元素
        """

        if self.is_empty():
            raise StackError('栈为空')
        else:
            self.__temp = self.__top
            self.__top = self.__top.next
            return self.__temp

    def get_top(self):
        """
            获取栈顶的元素（第一个）
        :return:
        """
        if self.is_empty():
            # raise StackError('栈为空')
            self.__print_info()
        else:
            return self.__top

    def show(self):
        if self.is_empty():
            self.__print_info()
        else:
            self.__temp = self.__top
            while self.__temp is not None:
                print(self.__temp.value)
                self.__temp = self.__temp.next

    def clear(self):
        """
            清空栈
        :return:
        """
        self.__top = None

    @staticmethod
    def __print_info(is_print=1):
        if is_print == 1:
            print('stack empty')


if __name__ == '__main__':
    stack = LinkStack()
    stack.push(1)
    stack.push(3)
    stack.push(5)
    # print(stack.top().value)
    print(stack.pop().value)
    print('-----')
    stack.show()
