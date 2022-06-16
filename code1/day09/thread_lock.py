#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022 2022/5/17 下午8:46
# @Author : tyler
# @File : thread_lock.py
# @Project : code1
import os
import time
from threading import Thread, Lock

all_ticket = ticket = 30
lock = Lock()


def huochepiao(name):
    global ticket
    while 1:
        time.sleep(0.01)
        lock.acquire()
        if ticket > 0:
            print(name + '售卖了一张票，座位号是：%s' % ('0' * (len(str(all_ticket)) - len(str(ticket))) + str(ticket)))
            ticket -= 1
            print('<<<<<剩余票数：%d' % ticket)
        else:
            print('车票已经卖完！')
            lock.release()
            os._exit(0)
            break
        lock.release()


if __name__ == '__main__':
    tl = []

    for i in range(5):
        t = Thread(target=huochepiao, args=('线程>>>%d' % i,))
        tl.append(t)
        t.start()
    for t in tl:
        t.join()
