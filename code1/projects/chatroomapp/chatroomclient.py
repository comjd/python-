#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022 2022/5/16 下午12:42
# @Author : tyler
# @File : chatroomclient.py
# @Project : code1
import os
import sys
from socket import *
from enumfile import InfoType
from multiprocessing import Process


class ChatRoomClient:
    def __init__(self, host='127.0.0.1', port=9090):
        self.__host = host
        self.__port = port
        self.__client = socket(AF_INET, SOCK_DGRAM)
        self.buffer_size = 1024
        self.__name = ''

    def __sendto_msg(self, msg, addr=''):
        if not addr:
            addr = (self.__host, self.__port)
        self.__client.sendto(msg.encode(), addr)

    def __recvfrom_msg(self):
        return self.__client.recvfrom(self.buffer_size)

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
            result += item + chart
        return result.strip()

    def do_login(self):
        while True:
            self.__name = input('请输入用户名：')
            if not self.__name.strip():
                print('用户名不能为空')
                continue
            self.__sendto_msg(ChatRoomClient.__msg_append_chart(' ', InfoType.login.value, self.__name))
            data, addr = self.__recvfrom_msg()
            if data.decode() == InfoType.login_success.value:
                print('您已成功进入聊天室')
                break
            print("\n用户名'{}'已存在，请重新输入。".format(self.__name))
            continue

    def __logout_chat(self):
        self.__sendto_msg(self.__msg_append_chart(' ', InfoType.logout.value, self.__name))

    def __send_chat(self):
        while True:
            try:
                msg = input('\n消息：')
            except KeyboardInterrupt or Exception:
                msg = 'quit'
            if msg == 'quit':
                self.__logout_chat()
                sys.exit()
            self.__sendto_msg(self.__msg_append_chart(' ', str(InfoType.chat.value), self.__name, msg))

    def __recv_chat(self):
        while True:
            try:
                msg, addr = self.__recvfrom_msg()
            except KeyboardInterrupt or Exception:
                sys.exit('退出聊天室')
            if msg.decode() == InfoType.logout.value:
                sys.exit('退出聊天室')
            print('\n' + msg.decode() + '\n消息：', end='')

    def main(self):
        self.do_login()
        pid = os.fork()
        if pid < 0:
            print('Error')
        elif pid == 0:
            self.__send_chat()
        else:
            self.__recv_chat()
        os.wait()
        # p1 = Process(target=self.__send_chat)
        # p1.start()
        # self.__recv_chat()
        # p1.join()


if __name__ == '__main__':
    c = ChatRoomClient()
    c.main()
