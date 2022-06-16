# -*- coding: utf-8 -*-
# @Time : 2022/5/13 下午10:05
# @Author : tyler
# @File : fork03.py
# @Project : code1

import os, sys
from time import sleep

pid = os.fork()

if pid < 0:
    print('Error')
elif pid == 0:
    print('the new process')
    # 进程退出，默认值为0，传入数字，若传入的值为非数字，控制台会打印相关信息
    sys.exit("退出")
else:
    sleep(1)
    print('the old process')
    print('child process id:', pid)
    print('parent process id:', os.getpid())

if __name__ == '__main__':
    pass
