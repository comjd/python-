# -*- coding: utf-8 -*-
# @Time : 2022/5/13 下午10:13
# @Author : tyler
# @File : fork04.py
# @Project : code1
from time import sleep
import os


def f1():
    for i in range(3):
        sleep(2)
        print('写代码')


def f2():
    for i in range(2):
        sleep(3)
        print('测代码')


pid = os.fork()

if pid < 0:
    print('Error')
elif pid == 0:
    f1()
else:
    f2()

if __name__ == '__main__':
    pass
