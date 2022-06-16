# -*- coding: utf-8 -*-
# @Time : 2022/5/13 下午10:21
# @Author : tyler
# @File : fork07.py
# @Project : code1
"""
    父线程处理僵尸线程，推荐
"""
import os
import signal
from time import sleep


def f1():
    for i in range(3):
        sleep(2)
        print('写代码')


def f2():
    for i in range(2):
        sleep(3)
        print('测代码')


# 处理僵尸进程
signal.signal(signal.SIGCHLD, signal.SIG_IGN)
pid = os.fork()

if pid < 0:
    print('Error')
elif pid == 0:
    print('the new process id', os.getpid())
    f2()

else:
    print('pid', os.getpid())
    # 父进程处理子进程
    f2()
    while True:
        pass

if __name__ == '__main__':
    pass
