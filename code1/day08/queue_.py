#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022 2022/5/16 下午9:12
# @Author : tyler
# @File : queue_.py
# @Project : code1

from multiprocessing import Queue, Process
from random import randint
from time import sleep

q = Queue(4)


def get_number():
    for i in range(6):
        num = randint(1, 33)
        q.put(num)
    q.put(randint(1, 16))


def print_number():
    sleep(1)
    l = []
    while True:
        sleep(0.0001)
        l.append(q.get())
        if q.empty():
            l[:-2].sort()
            print(l)
            break


if __name__ == '__main__':
    p1 = Process(target=get_number)
    p2 = Process(target=print_number)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
