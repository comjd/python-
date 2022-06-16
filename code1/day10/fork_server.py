#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022 2022/5/18 下午9:03
# @Author : tyler
# @File : fork_server.py
# @Project : code1
"""
    tcp多进程客户端
"""
import os
from signal import *
from socket import *

HOST = '0.0.0.0'
PORT = 9090
ADDR = (HOST, PORT)

s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(ADDR)
signal(SIGCHLD, SIG_IGN)
s.listen(5)
print('等链接...')


def handle(conn):
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(data.decode())
        conn.send(b'OK')
    conn.close()


while True:
    try:
        conn, addr = s.accept()
    except KeyboardInterrupt:
        os._exit()
    except Exception as e:
        print(e)
        continue
    print('客户端：%s链接成功', addr)
    pid = os.fork()
    if pid == 0:
        s.close()
        handle(conn)
        os._exit(0)
    else:
        conn.close()
