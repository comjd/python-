#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022 2022/5/17 上午11:31
# @Author : tyler
# @File : mythread.py
# @Project : code1
import time
from threading import Thread


class MyThread(Thread):
    def __init__(self, target=None, args=(), kwargs=None):
        super().__init__()
        self.target = target
        self.args = args
        self.kwargs = kwargs

    def run(self):
        print('step 1')
        time.sleep(2)
        self.target(*self.args, **self.kwargs)
        print('step 2')


def worker(sec, name):
    print('进入方法1...')
    time.sleep(sec)
    print(time.ctime(), name)


def worker1(sec, name):
    print('进入方法2...')
    time.sleep(sec)
    print(time.ctime(), name)


if __name__ == '__main__':
    mt = MyThread(target=worker, args=(5,), kwargs={'name': '张三'})
    mt.start()
    mt1 = MyThread(target=worker1, args=(2,), kwargs={'name': '历史'})
    mt1.start()
    mt1.join()
    mt.join()
