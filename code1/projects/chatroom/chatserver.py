# -*- coding: utf-8 -*-
# @Time : 2022/5/14 上午10:44
# @Author : tyler
# @File : chatserver.py
# @Project : code1

import os, sys
from socket import *
from enumfile import InfoType

ADDR = ('0.0.0.0', 9090)
user_info = {}


def process_msg(msg):
    if not msg:
        return None
    temp_msg = msg.split(' ')
    if temp_msg[0] == InfoType.chat.value:
        msg = ' '.join(temp_msg[2:])
        return temp_msg[0], temp_msg[1], msg
    return temp_msg[0], temp_msg[1]


def do_login(s, name, addr):
    if name in user_info:
        s.sendto('\n用户名：{}已存在'.format(name).encode(), addr)
        return
    s.sendto(InfoType.login_success.value.encode(), addr)
    msg = "\n欢迎'{}'进入聊天室".format(name)
    for user in user_info:
        s.sendto(msg.encode(), user_info[user])
    user_info[name] = addr


def do_chat(s, all_msg):
    """
        聊天
    :param s:
    :param all_msg:
    :return:
    """
    for i in user_info:
        if i != all_msg[1]:
            s.sendto((all_msg[1] + "：" + all_msg[2]).encode(), user_info[i])


def do_logout(s, all_msg):
    """
        退出聊天室
    :param s:
    :param all_msg:
    :return:
    """
    for i in user_info:
        if i != all_msg[1]:
            s.sendto('\n{}退出了聊天室'.format(all_msg[1]).encode(), user_info[i])
        else:
            s.sendto(InfoType.logout.value.encode(), user_info[all_msg[1]])
    del user_info[all_msg[1]]


def recv(s):
    try:
        data, addr = s.recvfrom(1024)
    except KeyboardInterrupt or Exception:
        return
    all_msg = process_msg(data.decode())
    print(all_msg)
    if all_msg[0] == InfoType.login.value:
        do_login(s, all_msg[1], addr)
    elif all_msg[0] == InfoType.chat.value:
        do_chat(s, all_msg)
    elif all_msg[0] == InfoType.logout.value:
        print(all_msg[0])
        do_logout(s, all_msg)


def send(s):
    try:
        msg = input('>>')
    except KeyboardInterrupt or Exception:
        return
    msg = InfoType.chat.value + ' ' + '管理员 ' + msg
    print(msg)
    s.sendto(msg.encode(), ADDR)


def main():
    s = socket(AF_INET, SOCK_DGRAM)
    s.bind(ADDR)
    pid = os.fork()
    if pid < 0:
        sys.exit('')
    elif pid == 0:
        while True:
            if send(s) is None:
                sys.exit()
    else:
        while True:
            if recv(s) is None:
                sys.exit("exit")


if __name__ == '__main__':
    main()
