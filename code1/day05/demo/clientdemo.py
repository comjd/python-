##!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022/5/13 下午3:37
# @Author : tyler
# @File : clientdemo.py
# @Project : code1
from socket import *


class Client:
    def __init__(self, host: str = '127.0.0.1', port: int = 9090):
        self.__host = host
        self.__port = port
        self.__server = socket()
        self.__conn = None
        self.buffer_size = 4096
        self.__data = b''
        self.__chars = ['utf-8', 'gbk', 'gb2312', 'ascii']
        self.msg = ''

    def start_tcp_client(self):
        temp = self.__client__init()
        if not temp[0]:
            print(temp[1])
            return
        while True:
            self.__send_msg()
            if not self.msg:
                break
        self.__socket_recv()
        print('Server:', self.__data.decode())
        self.__server.close()

    def start_udp_client(self):
        temp = self.__client__init(2)
        if not temp[0]:
            print(temp[1])
            return
        while True:
            # self.__sendto_msg()
            # if not self.msg:
            #     break
            self.__socket_recvfrom()
            print('Server:', self.__data.decode())
        self.__client.close()

    def __client__init(self, socket_type=1):
        if socket_type != 1:
            self.__server = socket(AF_INET, SOCK_DGRAM)
        else:
            try:
                self.__server.connect((self.__host, self.__port))
            except OSError as e:
                return False, e
            else:
                return True, None
        # 　服务端结束后是否立即释放端口
        self.__server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        # 绑定服务端的ip和端口

    def __socket_recv(self):
        """
        接收消息
        :return: 接收到的信息内容
        """
        # 收到消息的缓冲区大小
        try:
            self.__data = self.__server.recv(self.buffer_size)
        except ConnectionResetError:
            self.__data = b''
        else:
            if not self.__data or self.__data == '\r\n' or self.__data == b'\r\n':
                self.__data = b''

    def __data_to_str(self):
        """
            将字节数据转换为字符数据
        :return: 转换后的字符串
        """
        for char in self.__chars:
            try:
                return self.__data.decode(char, 'ignore').strip().strip(b'\x00'.decode())
            except UnicodeDecodeError as e:
                print('Error:%s' % e)
                continue
            except Exception:
                continue
        print(self.__data)
        return None

    def __send_msg(self):
        """
            发送消息
        """
        # self.msg = input('>>')
        # print(self.msg)
        with open('../log.txt', 'r') as f:
            while True:
                self.msg = f.readline()
                if not self.msg or self.msg == '\r\n':
                    return None
                self.__server.send(self.msg.encode())

    def __sendto_msg(self):
        self.msg = input('>>')
        self.__server.sendto(self.msg.encode(), (self.__host, self.__port))

    def __socket_recvfrom(self):
        """
        接收消息
        :return: 接收到的信息内容
        """
        # 收到消息的缓冲区大小
        try:
            self.__data, self.__conn = self.__server.recvfrom(self.buffer_size)
        except ConnectionResetError:
            self.__data = b''
        else:
            if not self.__data or self.__data == '\r\n' or self.__data == b'\r\n':
                self.__data = b''


if __name__ == '__main__':
    c = Client('192.168.10.100', 9090)
    # c.start_tcp_client()
    c.start_udp_client()
