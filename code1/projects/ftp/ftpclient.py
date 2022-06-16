#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022 2022/5/27 下午5:35
# @Author : tyler
# @File : ftpclient.py
# @Project : code1


import sys
import time
from socket import *
from infotype import InfoType
from fileprocess import FileProcess as fp


class FTPClient:
    def __init__(self, connfd):
        self.connfd = connfd

    def show_file_list(self):
        # while True:
        data = self.connfd.recv(1024)
        print(data.decode())

    def download_file(self, filename):
        data = self.connfd.recv(1024)
        if data.decode() == InfoType.PACKAGE_START.value:
            with open(filename, 'wb') as f:
                while True:
                    data = self.connfd.recv(4096)
                    if data[-len(InfoType.PACKAGE_END.value):] == InfoType.PACKAGE_END.value.encode():
                        f.write(data[:-len(InfoType.PACKAGE_END.value)])
                        break
                    f.write(data)
            print('下载成功')
        else:
            print(data.decode())

    def upload_file(self, filepath):
        if fp.is_file(filepath):
            data = self.connfd.recv(1024).decode()
            if data == InfoType.PACKAGE_START.value:
                for line in fp.read_line_file(filepath):
                    self.connfd.send(line)
                time.sleep(0.001)
                self.connfd.send(InfoType.PACKAGE_START.value.encode())
            else:
                print(data)
        else:
            print('上传的不是一个文件')

    def exit(self):
        self.connfd.send(InfoType.EXIT.value.encode())
        self.connfd.close()
        sys.exit('客户端退出')


def main():
    s = socket()
    s.connect(('127.0.0.1', 9090))
    client = FTPClient(s)
    while True:
        print('********************        list        ********************')
        print('********************        get file       ********************')
        print('********************        put file        ********************')
        print('********************        quit        ********************')
        try:
            data = input('>>')
        except KeyboardInterrupt:
            s.send(InfoType.EXIT.value.encode())
            sys.exit('进程退出')
            break
        except Exception as e:
            s.send(InfoType.EXIT.value.encode())
            print(e)
            break
        s.send(data.encode())
        if data.split(' ')[0].upper().strip() == InfoType.LIST.value:
            client.show_file_list()
        if data.split(' ')[0].upper().strip() == InfoType.DOWN.value:
            client.download_file(data.split(' ')[1])
        if data.split(' ')[0].upper().strip() == InfoType.UP.value:
            client.upload_file(data.split(' ')[1])
        if data.split(' ')[0].upper().strip() == InfoType.EXIT.value:
            client.exit()

        # s.send(data.encode())
        # data = s.recv(1024)
        # print(data.decode())


if __name__ == '__main__':
    main()
