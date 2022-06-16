# -*- coding: utf-8 -*-
# @Time : 2022/5/13 下午10:21
# @Author : tyler
# @File : fork07.py
# @Project : code1
"""
    父线程处理僵尸线程，wait()会阻塞，不推荐使用
"""
import os

pid = os.fork()

if pid < 0:
    print('Error')
elif pid == 0:
    print('the new process id', os.getpid())
else:
    os.wait()
    while True:
        pass

if __name__ == '__main__':
    pass
