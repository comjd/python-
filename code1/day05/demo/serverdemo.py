##!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022/5/13 下午1:53
# @Author : tyler
# @File : serverdemo.py
# @Project : code1
from socket import *


class Server:
    def __init__(self, host: str = '0.0.0.0', port: int = 9090):
        self.__host = host
        self.__port = port
        self.__server = socket()
        self.listen_num = 5
        self.__conn = None
        self.buffer_size = 4096
        self.__data = b''
        self.__chars = ['utf-8', 'gbk', 'gb2312', 'ascii']

    def start_tcp_server(self):
        temp = self.__server__init()
        if not temp[0]:
            print(temp[1])
        self.__server.listen(self.listen_num)
        while True:
            self.__conn, addr = self.__socket_accept()
            if addr is None:
                print(self.__conn)
                break
            while True:
                self.__socket_recv()
                if not self.__data:
                    print('客户端退出:', addr)
                    break
                print('收到客户端消息：%s' % self.__data_to_str())
                self.__send_msg()
            self.__conn.close()

    def start_udp_server(self):
        temp = self.__server__init(2)
        if not temp[0]:
            print(temp[1])
        while True:
            self.__socket_recvfrom()
            print('收到客户端消息：%s' % self.__data_to_str())
            # self.__send_msg()
        self.__client.close()

    def __server__init(self, socket_type=1):
        if socket_type != 1:
            self.__server = socket(AF_INET, SOCK_DGRAM)
        # 　服务端结束后是否立即释放端口
        self.__server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        # 绑定服务端的ip和端口
        try:
            self.__server.bind((self.__host, self.__port))
        except OSError as e:
            return False, e
        else:
            return True, None

    def __socket_accept(self):
        """
            等待连接的处理
        :return:
        """
        try:
            print('waiting...')
            return self.__server.accept()
        except KeyboardInterrupt:
            return 'server close...', None
        except Exception as e:
            return e, None

    def __socket_recv(self):
        """
        接收消息
        :return: 接收到的信息内容
        """
        try:
            # 收到消息的缓冲区大小
            self.__data = self.__conn.recv(self.buffer_size)
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
        msg = '200 ok'
        try:
            self.__conn.send(msg.encode())
        except ConnectionResetError:
            pass
        except ConnectionResetError:
            pass
        except Exception:
            pass

    def __socket_recvfrom(self):
        """
        接收消息
        :return: 接收到的信息内容
        """
        try:
            # 收到消息的缓冲区大小
            self.__data, self.__conn = self.__server.recvfrom(self.buffer_size)
        except ConnectionResetError:
            self.__data = b''
        else:
            if not self.__data or self.__data == '\r\n' or self.__data == b'\r\n':
                self.__data = b''


if __name__ == '__main__':
    # s = Server('192.168.100.30')
    s = Server()
    # s.start_tcp_server()
    s.start_udp_server()
    # print(s._Server.__data.decode('utf-8', 'ignore').strip().strip(b'\x00'.decode()))
