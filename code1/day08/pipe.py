#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022 2022/5/16 上午11:03
# @Author : tyler
# @File : pipe.py
# @Project : code1
from multiprocessing import Pipe, Process

fd1, fd2 = Pipe()


def app1():
    print('App1启动了')
    print('App1需要找App2完成验证')
    fd1.send('login')
    data = fd1.recv()
    print('收到App2验证完成的结果')
    print(data)


def app2():
    data = fd2.recv()
    if data == 'login':
        fd2.send(('zhang san', '123'))
    else:
        fd2.send('')
    print('App2已验证完成')


p1 = Process(target=app1)
p2 = Process(target=app2)
p1.start()
p2.start()
p1.join()
p2.join()
