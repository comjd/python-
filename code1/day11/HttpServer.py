#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022 2022/6/3 下午4:08
# @Author : tyler
# @File : HttpServer.py
# @Project : code1
import select
import time
from socket import *
from select import *
import queue


class HttpServer:
    def __init__(self, host='0.0.0.0', port=8001, resource_url=''):
        self.__host = host
        self.__port = port
        self.__resource_url = resource_url
        self.__addr = (host, port)
        self.__listen_number = 5
        self.__create_socket()
        self.__socket_bind()
        self.__rlist = []
        self.__wlist = []
        # self.__xlist = []
        self.__package_length = 4096
        self.message_queues = {}

    def __create_socket(self):
        self.__server = socket()
        self.__server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.__server.setblocking(0)

    def __socket_bind(self):
        self.__server.bind(self.__addr)

    def do_request(self, conn):
        data = conn.recv(self.__package_length)
        if not data:
            if conn in self.__wlist:
                self.__wlist.remove(conn)
            self.__rlist.remove(conn)
            conn.close()
            del self.message_queues[conn]
        else:
            self.message_queues[conn].put(data)
            if conn not in self.__wlist:
                self.__wlist.append(conn)

    def server_forever(self):
        self.__server.listen(self.__listen_number)
        self.__rlist.append(self.__server)
        print('http:127.0.0.1:%s/' % self.__port)
        while True:
            rs, ws, xs = select(self.__rlist, self.__wlist, self.__rlist)
            for r in rs:
                if r is self.__server:
                    conn, addr = self.__server.accept()
                    conn.setblocking(0)
                    self.__rlist.append(conn)
                    self.message_queues[conn] = queue.Queue()
                    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), '客户端{0}连接成功'.format(addr))
                else:
                    self.do_request(r)
            for w in ws:
                try:
                    next_msg = self.message_queues[w].get_nowait()
                except queue.Empty:
                    self.__wlist.remove(w)
                else:
                    info = next_msg.splitlines()[0].decode().split(" ")[1]
                    print(conn.getpeername(), ':', info)
                    if info == '/' or info[-5:] == '.html':
                        self.__get_html(conn, info)
                    else:
                        self.__get_data(conn)
            for s in xs:
                input.remove(s)
                for o in self.__wlist:
                    self.__wlist.remove(o)
                s.close()
                del self.message_queues[s]

    def __get_html(self, conn, info):
        filename = self.__resource_url + 'index.html' if info == '/' else self.__resource_url + info
        try:
            r = open(filename)
        except Exception as e:
            response = 'HTTP/1.1 404 Not Found\r\n'
            response += 'content-type:text/html\r\n'
            response += '\r\n'
            response += '<h1>Sorry,404</h1>'
        else:
            print('OK')
            response = 'HTTP/1.1 200 OK \r\n'
            response += 'content-type:text/html\r\n'
            response += '\r\n'
            response += r.read()
            r.close()
        finally:
            conn.send(response.encode())
            print('send over')

    def __get_data(self, conn):
        response = 'HTTP/1.1 404 Not Found\r\n'
        response += 'content-type:text/html\r\n'
        response += '\r\n'
        response += '<h1>Sorry...</h1>'
        conn.send(response.encode())


if __name__ == '__main__':
    server = HttpServer(resource_url='static/')
    server.server_forever()
