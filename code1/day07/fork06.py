# -*- coding: utf-8 -*-
# @Time : 2022/5/13 下午10:16
# @Author : tyler
# @File : fork05.py
# @Project : code1


"""
    产生僵尸进程
"""

import os
from time import sleep

pid = os.fork()

if pid < 0:
    print('Error')
elif pid == 0:
    sleep(1)
    print('the new process id',os.getpid())
else:
    while True:
        pass

if __name__ == '__main__':
    pass
