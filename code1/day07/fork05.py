# -*- coding: utf-8 -*-
# @Time : 2022/5/13 下午10:16
# @Author : tyler
# @File : fork05.py
# @Project : code1


"""
    产生孤儿进程
"""

import os
from time import sleep

pid = os.fork()

if pid < 0:
    print('Error')
elif pid == 0:
    sleep(1)
    print('the new process')
    print('child process id:', os.getpid())
    print('parent process id:', os.getppid())
else:
    print('the old process')
    print('child process id:', pid)
    print('parent process id:', os.getpid())

if __name__ == '__main__':
    pass
