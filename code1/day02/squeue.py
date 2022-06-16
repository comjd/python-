"""
    队列
"""


class QueueError(Exception):
    pass


class SQueue:
    def __init__(self):
        self.__queue = []

    def is_empty(self):
        """
            判断队列是否为空
        :return: True列表为空，False列表不为空
        """
        return self.__queue == []

    def join_queue(self, value):
        """
            将元素加入队列
        :param value:
        :return:
        """
        self.__queue.append(value)

    def out_queue(self):
        """
            出栈一个队列元素
        :return: 移除的元素
        """
        if self.is_empty():
            raise QueueError('queue empty')
        return self.__queue.pop(0)

    def clear(self):
        """
            清空队列
        """
        self.__queue = []

    def show(self):
        """
            显示所有队列中的元素
        """
        for q in self.__queue:
            print(q)


if __name__ == '__main__':
    que = SQueue()
    que.join_queue('99')
    que.join_queue('100')
    que.out_queue()
    # que.out_queue()
    print(que.is_empty())
    que.show()
