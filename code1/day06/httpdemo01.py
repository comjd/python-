#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022/5/12 下午9:32
# @Author : tyler
# @File : httpdemo01.py
# @Project : code1

from socket import *


def request(conn):
    data = conn.recv(4096)
    if not data:
        return
    info = data.decode().split('\r\n')[0].split(' ')[1]
    if info == '/':
        with open('demo01.html', 'r') as r:
            response = 'HTTP/1.1 200 OK \r\n'
            response += 'content-type:text/html\r\n'
            response += '\r\n'
            response += r.read()
    else:
        response = 'Http/1.1 200 OK\r\n'
        response += 'content-type:text/html\r\n'
        response += '\r\n'
        response += '<h1>sorry</h1>'
    conn.send(response.encode('utf-8'))


def start_server():
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(('0.0.0.0', 8001))
    s.listen(3)
    while True:
        conn, addr = s.accept()
        request(conn)


if __name__ == '__main__':
    start_server()
