#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022 2022/5/16 上午11:38
# @Author : tyler
# @File : chatroomserver.py
# @Project : code1
from socket import *
from enumfile import InfoType


class ChatRoomServer:
    __user = {}

    def __init__(self, host='0.0.0.0', port=9090):
        self.__host = host
        self.__port = port
        self.__server = socket(AF_INET, SOCK_DGRAM)
        self.buffer_size = 1024

    def do_request(self):
        """
            处理客户端发来的各种请求
        :return:
        """
        while True:
            data, addr = self.__recvfrom_msg()
            result = self.__splip_chart(data.decode())
            print(result)
            if result is not None:
                if result[0] == InfoType.login.value:
                    if self.do_login(result[1], addr):
                        self.__sendto_msg(InfoType.login_success.value, addr)
                    else:
                        self.__sendto_msg(InfoType.logout.value, addr)
                elif result[0] == InfoType.chat.value:
                    self.do_chat(result)
                elif result[0] == InfoType.logout.value:
                    self.do_logout(result)

    def main(self):
        try:
            self.__server.bind((self.__host, self.__port))
        except Exception as e:
            print('服务器绑定地址时发生错误：', e)
        self.do_request()

    def __sendto_msg(self, msg, addr=''):
        """
            发送消息
        :param msg: 消息内容
        :param addr: 消息接收地址
        """
        if not addr:
            addr = (self.__host, self.__port)
        self.__server.sendto(msg.encode(), addr)

    def __recvfrom_msg(self):
        """
            接收客户端的消息
        :return:
        """
        return self.__server.recvfrom(self.buffer_size)

    def __splip_chart(self, data='', chart=' '):
        """
            将客户端的消息默认按照空格进行切割
        :param data: 原消息内容
        :param chart: 切割的字符串
        :return: 切割后的数据字符串列表
        """
        if not data:
            return []
        chart_list = data.split(chart)
        if chart_list[0] == InfoType.chat.value:
            temp = ''.join(chart_list[2:])
            chart_list[2] = temp
        return chart_list

    def do_login(self, user, addr):
        """
            客户端登录问题处理
        :param user: 用户名称
        :param addr: 客户端地址
        :return: True登录成功，False登录失败
        """
        # 用户没在列表中
        if user not in ChatRoomServer.__user or user in '管理员':
            # 给群聊中的每个人发送欢迎新成员信息
            for item in ChatRoomServer.__user:
                self.__sendto_msg("\n欢迎'{}'进入聊天室".format(user), ChatRoomServer.__user[item])
            # 将信息用户保存值列表中
            ChatRoomServer.__user[user] = addr
            return True
        # 表示用户一在列表中存在
        return False

    def do_chat(self, msg):
        """
            聊天信息的处理
        :param msg:需要处理的聊天内容
        :return:
        """
        for user in ChatRoomServer.__user:
            # 将聊天信息转发给群里的其他所有人
            if user != msg[1]:
                self.__sendto_msg(msg[1] + '：' + msg[2], ChatRoomServer.__user[user])

    def do_logout(self, msg_list):
        """
            退出登录
        :param msg_list: 切割后的字符串列表
        :return:
        """
        for item in ChatRoomServer.__user:
            # 提醒群中用户某个用户退出了聊天室
            if item != msg_list[1]:
                self.__sendto_msg("\n'{}'退出了聊天室".format(msg_list[1]), ChatRoomServer.__user[item])
            else:
                # 给退出用户发送退出的消息，用户客户端退出进程程序
                self.__sendto_msg(InfoType.logout.value, ChatRoomServer.__user[msg_list[1]])
        # 从列表中删除用户信息
        if msg_list[1] in ChatRoomServer.__user:
            del ChatRoomServer.__user[msg_list[1]]


if __name__ == '__main__':
    server = ChatRoomServer()
    server.main()
