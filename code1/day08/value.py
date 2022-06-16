#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022 2022/5/17 上午9:00
# @Author : tyler
# @File : value.py
# @Project : code1
import random
import time
from multiprocessing import Value, Process
from ctypes import c_char_p

# 初始化内存共享，第一个参数是初始化的类型：i代表数字,f代表小数,c代表字节;第二个参数是值
# 注意内存共享类型一旦确定后就不能存储其他类型的数据
money = Value('i', 5000)  # 整数实例
chart = Value('c', b's')  # 字节实例
share_str = Value(c_char_p, b"asdfasdfa")  # 字符实例，不支持中文


def man():
    for i in range(30):
        time.sleep(0.2)
        money.value += random.randint(1, 1000)
        print('man:', money.value)


def girl():
    for i in range(30):
        time.sleep(0.1)
        money.value -= random.randint(100, 800)
        print('girl:', money.value)


def func():
    print(chart.value)
    chart.value = b'c'
    print(chart.value)


def func1():
    print(chart.value)


def f1():
    print(share_str.value.decode())
    share_str.value = b"sdfa"


def f2():
    print(share_str.value.decode())


if __name__ == '__main__':
    p = Process(target=f1)
    p0 = Process(target=f2)
    p.start()
    p0.start()
    p.join()
    p0.join()
    # p = Process(target=func)
    # p0 = Process(target=func1)
    # p.start()
    # p0.start()
    # p.join()
    # p0.join()
    # p1 = Process(target=man)
    # p2 = Process(target=girl)
    # p1.start()
    # p2.start()
    # p1.join()
    # p2.join()
    # print('总计余额：', money.value)
