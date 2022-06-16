#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022/5/13 上午9:25
# @Author : tyler
# @File : structserverdemo.py
# @Project : code1
from socket import *
import struct

# i表示整数　s表示字符 f表示浮点数
st = struct.Struct('i32sif')


def start_server():
    s = socket(AF_INET, SOCK_DGRAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(('0.0.0.0', 8003))
    while True:
        data, addr = s.recvfrom(1024)
        data = st.unpack(data)
        with open('student.txt', 'a') as f:
            f.write('%-3d %-10s %-3d %.1f\n' % (
            data[0], data[1].decode('utf-8', 'ignore').strip().strip(b'\x00'.decode()), data[2], data[3]))
            f.flush()


if __name__ == '__main__':
    start_server()
