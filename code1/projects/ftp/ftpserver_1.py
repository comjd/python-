#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022 2022/5/19 下午12:50
# @Author : tyler
# @File : ftpserver_1.py
# @Project : code1
import sys
from socket import *
from threading import Thread

from projects.ftp import infotype, fileprocess

HOST = '0.0.0.0'
PORT = 9090
ADDR = (HOST, PORT)
FTP_PATH = 'test_tcp_files'


class FTPServer(Thread):
    def __init__(self, conn):
        super().__init__()
        self.__server = conn

    def run(self):
        # self.__do_request()
        while True:
            data = self.__server.recv(1024)
            print(data.decode())

    def __do_request(self):
        data = self.__server.recv(1024)
        if data.decode() == infotype.InfoType.LIST.value:
            print(fileprocess.FileProcess.get_path_all_filenames(FTP_PATH))
            self.__send_msg(fileprocess.FileProcess.get_path_all_filenames(FTP_PATH))
        print(data)

    def __send_msg(self, msg):
        self.__server.send(msg.encode())


# class TCPServer:
#
#     def __init__(self):
#         self.__tcp_server = self.__create_server()
#
#     def get_server(self):
#         return self.__tcp_server
#
#     def __create_server(self):
#         self.__tcp_server = socket()
#         self.__tcp_server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
#         try:
#             self.__tcp_server.bind(ADDR)
#             self.__tcp_server.listen(5)
#             return self.__tcp_server
#         except KeyboardInterrupt:
#             sys.exit('服务端已退出...')
#         except Exception as e:
#             print(e)
#         return None


def main():
    # tcp = TCPServer()
    # server = tcp.get_server()
    # if server is not None:
    #     while True:
    #         conn, addr = server.accept()
    #         print('addr:', addr)
    #         ftp = FTPServer(conn)
    #         ftp.start()
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)
    s.listen(5)
    print('waiting...')
    while True:
        try:
            conn, addr = s.accept()
        except KeyboardInterrupt:
            sys.exit('服务推出')
        except Exception as e:
            print(e)
            continue
        print('客户端：', addr, '链接成功')
        t = FTPServer(conn)
        t.setDaemon(True)
        t.start()


if __name__ == '__main__':
    main()
