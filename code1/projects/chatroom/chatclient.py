# -*- coding: utf-8 -*-
# @Time : 2022/5/14 上午10:44
# @Author : tyler
# @File : chatclient.py
# @Project : code1
import os, sys
import signal
from socket import *
from enumfile import InfoType

ADDR = ('127.0.0.1', 9090)


def info_type_add_temp(info_type):
    return info_type + ' '


def recv_msg(s):
    try:
        data, addr = s.recvfrom(4096)
    except KeyboardInterrupt or Exception:
        sys.exit()
    if data.decode() == InfoType.logout.value:
        sys.exit()
    print(data.decode() + '\n消息内容>>', end='')


def send_msg(s, name):
    try:
        msg = input('消息内容>>')
    except KeyboardInterrupt or Exception:
        msg = 'quit'
    if msg == 'quit':
        s.sendto((info_type_add_temp(InfoType.logout.value) + name).encode(), ADDR)
        sys.exit('退出聊天室')
    msg = info_type_add_temp(InfoType.chat.value) + name + ' ' + msg
    s.sendto(msg.encode(), ADDR)


def recv_and_send_msg(s, name):
    signal.signal(signal.SIGCHLD, signal.SIG_IGN)
    pid = os.fork()
    if pid < 0:
        sys.exit('error')
    elif pid == 0:
        while True:
            send_msg(s, name)
    elif pid > 0:
        while True:
            recv_msg(s)


def enter_chat(s):
    """
        进入聊天室
    :param s: 客户端套接字
    :return:
    """
    while True:
        try:
            name = input('请输入姓名>>')
        except KeyboardInterrupt or Exception:
            sys.exit()
        s.sendto((info_type_add_temp(InfoType.login.value) + name).encode(), ADDR)
        msg, addr = s.recvfrom(1024)
        if msg.decode() == InfoType.login_success.value:
            print('进入聊天室成功')
            return name
        else:
            print(msg.decode())
            continue


def do_request(s):
    name = enter_chat(s)
    recv_and_send_msg(s, name)
    # logout(s, name)


def main():
    s = socket(AF_INET, SOCK_DGRAM)
    do_request(s)


if __name__ == '__main__':
    main()
