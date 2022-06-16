"""
    装饰器
"""

# def func03(func):
#     def wrapper():
#         print('开始执行行功能')
#         return func()
#
#     return wrapper
#
#
# @func03
# def func01():
#     print('func01被执行了')
#
#
# @func03
# def func02():
#     print('func02被执行了')
#
#
# func01()
# func02()
import time


def func04(func):
    def wrapper(*args, **kwargs):
        print('开始执行新功能', args)
        return func(*args, **kwargs)

    return wrapper


@func04
def func05(name):
    print('func01被执行了', name)


@func04
def func06(age):
    print('func02被执行了', age)


func05('你好')
func06(345)


def print_execute_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(end_time - start_time)
        return result

    return wrapper


@print_execute_time
def func07():
    result = 0
    for i in range(10000):
        result += i
    print(result)


@print_execute_time
def func08(number):
    result = 0
    for i in range(number):
        result += i
    print(result)


print('------------------')
func07()
func08(100000000)
