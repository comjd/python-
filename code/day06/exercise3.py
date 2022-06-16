class Wife:
    count = 0

    def __init__(self):
        Wife.count += 1

    @classmethod
    def print_count(cls):
        print('总共创建了', cls.count, '个对象')


w01 = Wife()
w02 = Wife()
w03 = Wife()
w04 = Wife()
w05 = Wife()
w06 = Wife()

Wife.print_count()
