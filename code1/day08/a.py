# -*- coding: utf-8 -*-
# @Time : 2022/5/15 上午10:32
# @Author : tyler
# @File : multiprocess02.py
# @Project : code1

from multiprocessing import Process


def f1(a):
    print('f1:', a)


def f2(b):
    pr