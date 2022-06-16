#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022 2022/6/1 下午9:30
# @Author : tyler
# @File : tcpclient.py
# @Project : code1
from socket import *


def main():
    s = socket()
    s.connect(('127.0.0.1', 9090))
    print('服务器连接成功.')
    while True:
        data = input('>>')
        s.send(data.encode())
        data = s.recv(1024)
        if not data:
            return False
        print('Server', data.decode())


if __name__ == '__main__':
    flag = True
    while flag:
        flag = not main()
        print('链接已断开，正在重新连接，请稍后。。。')
        # main()
