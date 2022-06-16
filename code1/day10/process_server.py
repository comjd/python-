#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022 2022/5/18 下午9:39
# @Author : tyler
# @File : process_server.py
# @Project : code1

"""
    tcp多进程客户端
"""
import os
from signal import *
from socket import *
from multiprocessing import Process

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
        os._exit(0)
    except Exception as e:
        print(e)
        continue
    print('客户端：', addr, '链接成功')
    p = Process(target=handle, args=(conn,))
    p.daemon = True  # 主进程结束所有子进程也退出
    p.start()
