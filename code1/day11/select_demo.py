#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022 2022/6/2 下午1:30
# @Author : tyler
# @File : select_demo.py
# @Project : code1

# 通过非阻塞io实现http请求
# select + 回调 + 事件循环

# 使用单线程完成高并发

import select
import socket
import sys
from queue import Queue
import queue


def main():
    # 创建套接字
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.setblocking(False)
    server.bind(('0.0.0.0', 9090))
    # 监听传入的连接
    server.listen(5)

    """
    第一个是要检查要读取的传入数据的对象列表，
    第二个包含在缓冲区中有空间时将接收传出数据的对象，
    第三个包含可能有错误的对象（通常是错误的组合输入和输出通道对象）。
    """
    input = [server]  # 从中读取数据
    output = []  # 将数据发送出去
    select.select(input, output, input)

    message_queue = {}  # 消息队列

    while input:
        # 等待至少一个套接字准备好处理
        print(sys.stderr, '\nwaiting for the next event')
        """
        readable中的socket连接代表有数据可接受，可读取
        writable list中存放着你可以对其进行发送(send)操作
        exceptional 当连接通信出现error时会把error写到exceptional列表中
        """
        readable, writable, exceptional = select.select(input, output, input)

        """
        readable列表中的socket可能会有3种可能状态，
            1. 如果这个socket是server(它负责监听客户端的连接)，那就表示server端已经收到一个新的连接
            2. 客户端把数据发送过来了
            3. 客户端和服务器端断开了连接，将客户端对象从 列表和队列中删除
        """
        for s in readable:
            if s is server:  # 第一种情况，表示有新的连接进来
                connection, add = s.accept()  # 接受新的连接
                connection.setblocking(0)

                """
                这个时候，为了不阻塞整个程序的运行，我们先将它放入input列表中。
                下一次loop时，就会被select去监听，如果这个连接的客户端发来了数据
                那么这个连接的fd在server端就会变成就绪的，select就会把这个连接返回到readable列表中
                然后在 for s in readable中取出这个连接，开始接受数据
                """
                input.append(connection)
                message_queue[connection] = Queue()

            else:  # 第2种情况就是，客户端把数据发送了过来
                data = s.recv(1024)  # 通过recv去接受数据
                if data:
                    print(sys.stderr, 'received "%s" from %s' % (data, s.getpeername()))
                    message_queue[s].put(data)  # 接受到的数据先放到队列中
                    if s not in output:
                        output.append(s)  # 为了不影响处理与其他客户端的连接，这里不立刻返回数据给客户端
                else:  # 第3种情况 就是客户端断开了连接，这个时候recv()数据就是空，这个时候就可以跟客户端断开连接
                    if s in output:
                        """
                        既然断开了连接，就没有必要给客户端发送数据了
                        如果客户端连接对象还在output中，就把他删除
                        """
                        output.remove(s)
                    input.remove(s)  # 在input列表中也删除掉
                    # 关闭连接，在队列中也删除
                    s.close()
                    del message_queue[s]

        """
        writable list也有几种状态，如果客户端连接在跟它对应的queue里有数据时，就把这个数据取出来再发给用户
        否则就把这个连接从output中移除，这样下一次，select调用时检测到output列表中没有这个连接，就会认为这个连接处于非活动状态
        """
        for s in writable:
            try:
                next_msg = message_queue[s].get_nowait()
            except queue.Empty as e:
                output.remove(s)
            else:
                s.send(next_msg)

        """
        如果跟某个socket连接通信失败出现错误，就把这个连接对象从 各个列表中删除，再关闭连接
        """
        for s in exceptional:
            input.remove(s)
            for o in output:
                output.remove(o)
            s.close()
            del message_queue[s]


if __name__ == '__main__':
    main()
