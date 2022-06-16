#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022 2022/5/17 下午8:15
# @Author : tyler
# @File : thread_event.py
# @Project : code1
import time
from threading import Event, Thread

kouhao = None  # 用于线程通信的全局变量


def say():
    print('说口号了')
    global kouhao
    kouhao = '大王叫我来寻山'
    print('口号是：', kouhao)
    e.set()  # 操作完共享资源　e　设置


if __name__ == '__main__':
    e = Event()
    t = Thread(target=say)
    t.start()
    e.wait()  # 阻塞，等待线程完成执行
    print('开始对口号')
    if kouhao != '大王叫我来寻山':
        print('坏人。。。杀了他')
    else:
        print('都自己人')
    t.join()
