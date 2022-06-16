# -*- coding: utf-8 -*-
# @Time : 2022/5/13 下午10:21
# @Author : tyler
# @File : fork07.py
# @Project : code1
"""
    父线程处理僵尸线程，双重子线程,比较复杂，不太推荐
"""
import os
import sys
from time import sleep


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
    print('the new process id', os.getpid())
    id = os.fork()
    if id < 0:
        print('2 Error...')
    elif id == 0:
        print('new', os.getppid(), ' new new', os.getpid())
        f1()
    else:
        print('1 new', os.getpid())
        sys.exit('1^^^^')

else:
    print('pid', os.getpid())
    # 父进程处理子进程
    os.wait()
    f2()
    while True:
        pass

if __name__ == '__main__':
    pass
