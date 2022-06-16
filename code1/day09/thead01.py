#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022 2022/5/17 上午10:57
# @Author : tyler
# @File : thead01.py
# @Project : code1
import os
import random
import time
from threading import Thread


def worker():
    for i in range(6):
        time.sleep(0.4)
        print('01:', i, os.getpid())


def worker1():
    for i in range(6):
        time.sleep(0.5)
        print('02>>', random.randint(1, 100), os.getpid())


td = Thread(target=worker)
td1 = Thread(target=worker1)
td.start()
td1.start()
td.join()
td1.join()

if __name__ == '__main__':
    pass
