# -*- coding: utf-8 -*-
# @Time : 2022/5/15 上午10:17
# @Author : tyler
# @File : multiprocess01.py
# @Project : code1


import multiprocessing as mp
import os
import time


def func():
    time.sleep(3)
    print('我是子进程的打印的')


print('pid=', os.getpid())
p = mp.Process(target=func())
p.start()
print('父进程打印的。')
p.join()
