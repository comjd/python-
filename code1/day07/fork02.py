# -*- coding: utf-8 -*-
# @Time : 2022/5/13 下午9:25
# @Author : tyler
# @File : fork02.py
# @Project : code1
"""
    生成一个子进程，获取进程的PID和父进程的PID
"""
import os

pid = os.fork()

if pid < 0:
    print('Error')
elif pid == 0:
    print('the new process')
    print('child process id:', os.getpid())
    print('parent process id:', os.getppid())
else:
    print('the old process')
    print('child process id:', pid)
    print('parent process id:', os.getpid())


if __name__ == '__main__':
    pass
