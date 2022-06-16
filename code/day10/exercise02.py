"""
    闭包
        内部函数
        内部函数调用外部函数变量或者函数
        外部函数返回内部函数
"""


def func01(name):
    """
        有参数无返回值
    :param name:
    :return:
    """
    print('func01执行')

    def func02():
        print(name)

    return func02


# f=func01('你好')
# f()


def func02(name):
    """
        有参数有返回值
    :param name:
    :return:
    """
    print('func02执行')

    def func03():
        nonlocal name
        print(name)
        name = '娃哈哈' + name
        return name

    return func03


# f = func02('王皓')
# print(f())


def func03():
    """
        无参数无返回值
    """
    print('func03执行')
    name = '忘记了'

    def func04():
        nonlocal name
        name = '娃哈哈' + name
        print(name)

    return func04


f = func03()
f()
