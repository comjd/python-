class QueueError(Exception):
    pass


class LinkNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class LQueue:
    def __init__(self):
        self.__head = LinkNode(None)
        self.__bottom = self.__head
        self.__temp = self.__head

    def is_empty(self):
        """
            判断队列是否为空
        :return: True列表为空，False列表不为空
        """
        return self.__head == self.__bottom

    def join_queue(self, value):
        """
            将元素加入队列
        :param value:
        :return:
        """
        self.__bottom.next = LinkNode(value)
        self.__bottom = self.__bottom.next

    def __get_next_link_node(self):
        """
            获取链表下一个元素
        :return:
        """
        while self.__temp is not None:
            yield self.__temp
            self.__temp = self.__temp.next

    def out_queue(self):
        """
            出栈一个队列元素
        :return: 移除的元素
        """
        if self.is_empty():
            raise QueueError('queue empty')
        else:
            # self.__temp = self.__head.next
            self.__head = self.__head.next
            return self.__head

    def clear(self):
        """
            清空队列
        """
        self.__bottom = self.__head = LinkNode(None)

    def show(self):
        """
            显示所有队列中的元素
        """
        self.__temp = self.__head.next
        for q in self.__get_next_link_node():
            print(q.value)
        print('-##########')
        print(self.__head.next.value)
        print(self.__bottom.value)
        print('-##########')


if __name__ == '__main__':
    que = LQueue()
    que.join_queue('9999')
    que.join_queue('88')
    que.join_queue('8890')
    que.join_queue('lkk')
    que.show()
    print(que.out_queue().value)
    print(que.out_queue().value)    
    que.clear()
    print(que.is_empty())