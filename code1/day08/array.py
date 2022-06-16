#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022 2022/5/17 上午9:54
# @Author : tyler
# @File : array.py
# @Project : code1
from multiprocessing import Array, Process
from time import sleep


def worker(arr):
    print(arr.value)
    arr[0]=b'H'


if __name__ == '__main__':
    arr = Array('c', b'hello')
    p = Process(target=worker(arr))
    # p0 = Process(target=f2)
    p.start()
    # p0.start()
    p.join()
    print(arr.value.decode())
    # p0.join()