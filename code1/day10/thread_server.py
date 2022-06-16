#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022 2022/5/18 下午10:05
# @Author : tyler
# @File : thread_server.py
# @Project : code1
import sys
from socket import *
from threading import Thread
import os

HOST = '0.0.0.0'
PORT = 9090
ADDR = (HOST, PORT)


def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'OK')
    c.close()


s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(ADDR)
s.listen(5)
print('waiting...')
while True:
    try:
        conn, addr = s.accept()
    except KeyboardInterrupt:
        sys.exit('服务推出')
    except Exception as e:
        print(e)
        continue
    print('客户端：',addr,'链接成功')
    t = Thread(target=handle, args=(conn,))
    t.setDaemon(True)
    t.start()
