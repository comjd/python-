class LinkNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class LinkList:
    def __init__(self):
        self.__head = LinkNode(None)
        self.__temp = self.__head

    @property
    def head(self):
        return self.__head

    def init_link_list(self, list_):
        """
            根据列表初始化链表
        :param list_: 列表数据
        :return: 返回所有链表数据
        """
        self.__temp = self.__head
        for i in list_:
            self.__temp.next = LinkNode(i)
            self.__temp = self.__temp.next

    def __get_next_link_node(self):
        """
            获取链表下一个元素
        :return:
        """
        while self.__temp is not None:
            yield self.__temp
            self.__temp = self.__temp.next

    def last(self):
        """
        获取最后一个元素
        :return:
        """
        self.__temp = self.__head
        for node in self.__get_next_link_node():
            if node.next is None:
                return node

    def first(self):
        """
            获取链表的第一个元素
        :return: 返回链表的第一个元素
        """
        if self.__head.next is not None:
            return self.__head.next
        return self.__head

    def show_link_list(self):
        """
            打印所有的链表数据
        """
        self.__temp = self.__head.next
        for node in self.__get_next_link_node():
            print(node.value)

    def clear(self):
        """
        清空链表数据
        """
        self.__head.next = None

    def append(self, value):
        """
            在链表最后追加元素
        :param value:
        """
        self.last().next = LinkNode(value)

    def insert(self, index, value):
        """
            在指定位置插入元素
        :param index: 需要插入元素的位置
        :param value: 元素的值
        """
        self.__temp = self.__head
        for node in self.__get_next_link_node():
            if index <= 0 or node.next is None:
                new_node = LinkNode(value)
                new_node.next = node.next
                node.next = new_node
                break
            index -= 1

    def remove(self, value):
        """
            根据元素的值移除链表中的对应元素
        :param value: 需要移除元素的值
        """
        self.__temp = self.__head
        for link_node in self.__get_next_link_node():
            if link_node.next is not None and link_node.next.value == value:
                link_node.next = link_node.next.next

    def get_next_link_node(self):
        """
            获取一个链表元素
        :return: 返回一个链表中的元素
        """
        self.__temp = self.__head.next
        for link_node in self.__get_next_link_node():
            yield link_node

    def get_index_value(self, index):
        """
            根据链表的下标获取对应的值
        :param index: 下标位置
        :return: 下标对应的值
        """
        self.__temp = self.__head.next
        for node in self.__get_next_link_node():
            if index <= 0:
                return node.value
            index -= 1
        raise IndexError('下标越界')




if __name__ == '__main__':
    link_list = LinkList()
    link_list.init_link_list([item for item in range(10)])
    # link_list.show_link_list()
    # link_list.clear()
    link_list.show_link_list()
    link_list.append('jk')
    print(link_list.last().value)
    print(link_list.first().value)
    link_list.insert(0, 'jakdjf')
    link_list.remove('jk')
    print('------')
    link_list.show_link_list()
    print('-----------')
    print(link_list.get_index_value(10))
