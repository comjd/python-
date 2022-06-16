#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022 2022/5/17 上午11:02
# @Author : tyler
# @File : thead02.py
# @Project : code1

from threading import Thread
import os, time, random


def f1():
    print(time.ctime())


def f2():
    time.sleep(0.2)
    print(random.random())


def f3():
    s=os.popen('ping www.baidu.com')
    print(s.read())


if __name__ == '__main__':
    arr = [f1, f2, f3]
    arr_join = []
    for i in arr:
        t = Thread(target=i)
        t.start()
        arr_join.append(t)
    for i in arr_join:
        i.join()
