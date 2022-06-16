# -*- coding: utf-8 -*-
# @Time : 2022/5/15 上午10:32
# @Author : tyler
# @File : multiprocess02.py
# @Project : code1

from multiprocessing import Process


def f1(a):
    print('f1:', a)


def f2(b):
    print('f2:', b)


def f3(d):
    print('f3:', d)


func_list = [f1, f2, f3]
p_list = []

for f in func_list:
    p = Process(target=f, args=(1,))
    p_list.append(p)
    p.start()

for a in p_list:
    a.join()
