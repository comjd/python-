"""
    排序linklist
"""
import random

from day01.linklist import LinkList


class LinkListHelper:
    @staticmethod
    def merge(link1, link2):
        """
            链表合并
        :param link1: 主合并链表
        :param link2: 被合并链表
        :return: 返回主合并链表
        """
        p = link1.head
        q = link2.head.next
        while p.next is not None:
            if p.next.value < q.value:
                p = p.next
            else:
                tmp = p.next
                p.next = q
                q = tmp
                p = p.next
        p.next = q
        return link1


if __name__ == '__main__':
    l01 = LinkList()
    l01.init_link_list(sorted([random.randint(0, 1000) for i in range(31)]))
    l01.show_link_list()
    print('------')
    l02 = LinkList()
    l02.init_link_list(sorted([random.randint(1, 1000) for i in range(3)]))
    l02.show_link_list()
    print('--------------')
    temp = LinkListHelper.merge(l01, l02)
    temp.show_link_list()