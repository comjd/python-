#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022 2022/6/3 下午3:28
# @Author : tyler
# @File : gevent_exercise.py
# @Project : code1

import gevent
from gevent import monkey

monkey.patch_time()
from time import sleep


def foo(a, b):
    print('foo start...', a, b)
    sleep(3)
    print('foo end...')


def bar():
    print('bar start ...')
    sleep(2)
    print('bar end ...')


if __name__ == '__main__':
    a = gevent.spawn(foo, 2, 3)
    b = gevent.spawn(bar)
    gevent.joinall([a, b])
