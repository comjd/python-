#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022 2022/5/27 下午5:31
# @Author : tyler
# @File : ftpserver.py
# @Project : code1
import sys
import time
from socket import *
from threading import Thread
from infotype import InfoType
from fileprocess import FileProcess as fp

HOST = '0.0.0.0'
PORT = 9090
ADDR = (HOST, PORT)
FTP_PATH = 'test_tcp_files/'


class FTPServer(Thread):
    def __init__(self, connfd):
        self.connfd = connfd
        super().__init__()

    def run(self):
        while True:
            try:
                data = self.connfd.recv(1024).decode()
                print(data)
            except ConnectionResetError:
                continue
            if data.split(' ')[0].upper() == InfoType.LIST.value:
                self.show_file_list()
            elif data.split(' ')[0].upper() == InfoType.DOWN.value:
                self.download_file(data.split(' ')[1])
            elif data.split(' ')[0].upper() == InfoType.UP.value:
                self.upload_file(data.split(' ')[1])
            elif data.split(' ')[0].upper() == InfoType.EXIT.value:
                self.exit()
                break

    def show_file_list(self):
        result = ''
        for file in fp.get_path_all_filenames(FTP_PATH):
            result += file + '\n'
        self.connfd.send(result.encode())

    def download_file(self, filename):
        print(FTP_PATH + filename)
        if fp.file_exists(FTP_PATH + filename):
            print(filename)
            self.connfd.send(b'ok')
            time.sleep(0.001)
            for line in fp.read_line_file(FTP_PATH + filename):
                self.connfd.send(line)
            time.sleep(0.001)
            self.connfd.send('####'.encode())
        else:
            self.connfd.send('文件不存在'.encode())

    def upload_file(self, filename):
        if fp.file_exists(FTP_PATH + filename):
            self.connfd.send('文件已存在'.encode())
        else:
            self.connfd.send(b'OK')
            with open(FTP_PATH + filename, 'wb') as f:
                while True:
                    data = self.connfd.recv(1024)
                    if data[-4:] == '####'.encode():
                        print('over')
                        f.write(data[:-4])
                        f.flush()
                        break
                    else:
                        f.write(data)
                        f.flush()

    def exit(self):
        print('客户端{0}退出'.format(self.connfd.getpeername()))
        self.connfd.close()


def main():
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)
    s.listen(5)
    while True:
        print('waiting...')
        try:
            conn, addr = s.accept()
        except KeyboardInterrupt:
            sys.exit('服务退出')
        except Exception as e:
            print(e)
            continue
        print('客户端：', addr, '链接成功')
        t = FTPServer(conn)
        t.setDaemon(True)
        t.start()


if __name__ == '__main__':
    main()
