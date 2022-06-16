#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022/5/13 上午9:37
# @Author : tyler
# @File : structclientdemo.py
# @Project : code1
from socket import *
import struct

st = struct.Struct('i32sif')


def start_client():
    s = socket(AF_INET, SOCK_DGRAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    while True:
        # id = int(input('ID:'))
        # name = input('NAME:')
        # age = int(input('AGE:'))
        # score = int(input('SCORE:'))
        id = __str_to_int("input('ID:')")
        name = input('NAME:')
        age = __str_to_int("input('AGE:')")
        score = __str_to_int("input('SCORE:')")
        s.sendto(st.pack(id, name.encode(), age, score), ('127.0.0.1', 8003))


def __str_to_int(value):
    while True:
        try:
            data = eval(value)
            return int(data)
        except Exception:
            print('请重新输入数字')
            continue


if __name__ == '__main__':
    start_client()
