#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022 2022/6/3 下午3:51
# @Author : tyler
# @File : gevent_socket.py
# @Project : code1
import gevent
from gevent import monkey

monkey.patch_socket()
from socket import *


def handle(conn):
    while True:
        data = conn.recv(1024)
        if data:
            print(data.decode())
            conn.send(b'OK')
        else:
            break


def main():
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(('0.0.0.0', 9090))
    s.listen(5)
    print('waiting...')
    while True:
        conn, addr = s.accept()
        print('客户端{0}连接上了'.format(addr))
        gevent.spawn(handle, conn)  # 变为协程


if __name__ == '__main__':
    main()
