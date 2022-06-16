# -*- coding: utf-8 -*-
# @Time : 2022/5/15 下午7:54
# @Author : tyler
# @File : exercise01.py
# @Project : code1
"""
    将一个文件切割为上下2部分,分别复制到不同的文件中，通过多进程实现
"""
import math
import os
import time
import wave

from multiprocessing import Pool

file_size = os.path.getsize('multiprocess02.py')


def write_up_file():
    with open('a.py', 'wb'):
        pass
    wf = open('a.py', 'ab')
    with open('multiprocess02.py', 'rb') as f:
        for i in range(0, math.ceil(file_size / 2), 100):
            data = f.read(100)
            size = f.tell()
            if size > (file_size // 2):
                data = data[0:(file_size//2) % 100]
            wf.write(data)
            wf.flush()
    wf.close()


def write_down_file():
    with open('b.py', 'wb'):
        pass
    wf = open('b.py', 'ab')
    with open('multiprocess02.py', 'rb') as f:
        size = f.seek(file_size // 2)
        while True:
            data = f.read(100)
            if not data:
                break
            wf.write(data)
            wf.flush()

    wf.close()
    f.close()


p1 = Pool(2)
p1.apply_async(func=write_up_file)
p1.apply_async(func=write_down_file)
p1.close()
p1.join()

if __name__ == '__main__':
    pass
