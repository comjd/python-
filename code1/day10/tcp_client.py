#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022 2022/5/18 下午9:20
# @Author : tyler
# @File : tcp_client.py
# @Project : code1
import os
import sys
from socket import *

s = socket()
s.connect(('127.0.0.1', 9090))
while True:
    try:
        data = input('>>')

    except KeyboardInterrupt:
        sys.exit('进程退出')
        break
    except Exception as e:
        print(e)

    s.send(data.encode())
    data = s.recv(1024)
    print(data.decode())
