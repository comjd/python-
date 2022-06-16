#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022/5/12 下午8:58
# @Author : tyler
# @File : httpresponse.py
# @Project : code1
from socket import *

s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 8001))
s.listen(5)
c, addr = s.accept()
data = c.recv(4096)
print(data)
response = """
HTTP/1.1 200 OK
content-type:text/html

<h1>您好啊！</h1>
"""
c.send(response.encode('gbk'))
c.close()
s.close()

# if __name__ == '__main__':
#     pass
