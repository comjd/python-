#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022 2022/6/1 下午1:59
# @Author : tyler
# @File : select_exercise.py
# @Project : code1


from select import select
from socket import *


def main():
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(('0.0.0.0', 9090))
    s.listen(5)
    rlist = [s]
    wlist = []
    xlist = []
    while True:
        print('waiting...')
        rs, ws, xs = select(rlist, wlist, xlist)
        for r in rs:
            if r is s:
                conn, addr = r.accept()
                rlist.append(conn)
                print('客户端连接成功', addr)
            else:
                data = r.recv(1024)
                # try:
                #     data = r.recv(1024)
                # except ConnectionResetError:
                #     rlist.remove(r)
                #     continue
                if not data.decode():
                    print(r.getpeername(), '退出了连接')
                    rlist.remove(r)
                    r.close()
                    continue
                print(data.decode())
                r.send(b'OK')

        for w in ws:
            pass
        for x in xs:
            pass


if __name__ == '__main__':
    main()
