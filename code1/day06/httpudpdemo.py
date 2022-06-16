#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022/5/13 上午8:57
# @Author : tyler
# @File : httpudpdemo.py
# @Project : code1
from socket import *


def start_server():
    s = socket(AF_INET, SOCK_DGRAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(('127.0.0.1', 8002))
    while True:
        print('----')
        data, addr = s.recvfrom(4096)
        print('success...', addr)
        if not data:
            continue
        print(data.decode())
        response = """
            HTTP/1.1 200 OK
            content-type:text/html
            
            <h1>您好啊！</h1>
        """
        s.sendto(response.encode(), addr)


if __name__ == '__main__':
    start_server()
