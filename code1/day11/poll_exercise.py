#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022 2022/6/1 下午9:52
# @Author : tyler
# @File : poll_exercise.py
# @Project : code1
import sys
from select import *
from socket import *


def main():
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(('0.0.0.0', 9090))
    s.listen(5)
    dicks = {s.fileno(): s}
    p = poll()
    p.register(s, POLLIN | POLLERR)
    while True:
        print('waiting...')
        events = p.poll()
        for sk, e in events:
            if sk == s.fileno():
                conn, addr = dicks[sk].accept()
                print(addr, '连接成功')
                dicks[conn.fileno()] = conn
                p.register(conn, POLLIN | POLLERR)
            elif e & POLLIN:
                try:
                    data = dicks[sk].recv(1024)
                except ConnectionResetError:
                    del dicks[sk]
                    p.unregister(sk)
                    continue
                if not data:
                    print(sys.stderr, '关闭', )
                    del dicks[sk]
                    p.unregister(sk)
                    dicks[sk].close()
                    continue
                print(data.decode())
                dicks[sk].send(b'OK')
            elif e & POLLERR:
                pass


if __name__ == '__main__':
    main()
