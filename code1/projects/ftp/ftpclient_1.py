#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022 2022/5/19 下午2:10
# @Author : tyler
# @File : ftpclient_1.py
# @Project : code1
import os
import sys
from socket import *
from fileprocess import *
from projects.ftp.infotype import InfoType
from multiprocessing import Process


class FTPClient:
    def __init__(self, server_host='127.0.0.1', server_port=9090):
        self.__host = server_host
        self.__port = server_port
        self.__client = self.__create_client()
        self.buffer_size = 1024

    def __create_client(self):
        self.__client = socket()
        try:
            self.__client.connect((self.__host, self.__port))
            return self.__client
        except KeyboardInterrupt:
            sys.exit('客户端退出')
        except Exception as e:
            print(e)
        return None

    def get_recv_msg(self):
        data = self.__recv_msg()

    @staticmethod
    def __msg_append_chart(chart=' ', *args):
        """
            在每个字符串的结尾拼接制定的字符串，拼接的字符串主要用于服务端的消息分割，默认为' '
        :param chart:结尾拼接的字符串
        :param args:需要拼接的字符串
        :return:拼接后的字符串
        """
        result = ''
        for item in args:
            result += chart.join(item)
        return result.strip()

    def __send_msg(self, msg):
        self.__client.send(msg.encode())

    def __recv_msg(self):
        return self.__client.recv(self.buffer_size)

    def __show_file_list(self):
        msg = self.__msg_append_chart(' ', (InfoType.LIST.value,))
        self.__send_msg(msg)

    def send_info(self):
        while True:
            infotype = input(
                """
                ******************************
                1.查询文件
                2.下载文件
                3.上传文件
                ******************************
                """)
            if infotype == "1":
                self.__show_file_list()
            else:
                print('编号错误，重新输入')
                continue

    def recv_info(self):
        while True:
            data = self.__recv_msg()


def main():
    c = FTPClient()
    c.send_info()
    # p = Process(target=c.send_info())
    # p.start()
    # print('开始等...')
    # c.recv_info()
    # p.join()
    # pid = os.fork()
    # if pid == 0:
    #     c.send_info()
    # else:
    #     print('dengd')
    #     c.recv_info()


if __name__ == '__main__':
    main()
