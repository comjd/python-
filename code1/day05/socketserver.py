# !/user/bin/env python
# coding=utf-8
from socket import *


class SocketServer:

    def __init__(self, host='0.0.0.0', port=8899):
        self.__host = host
        self.__port = port
        self.listen_num = 5
        self.buffer_size = 1024
        self.__data = ''

    def tcp_server(self):
        with socket() as server:
            server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
            server.bind((self.__host, self.__port))
            server.listen(self.listen_num)
            while True:
                print('TCP server waiting...')
                conn, addr = self.__accept(server)
                if not addr:
                    print(conn)
                    break
                while True:
                    self.__data = conn.recv(self.buffer_size)
                    if not self.__data or self.__data == '\r\n':
                        break
                    print('接收到客户端：的消息:%s' % self.__data.decode('utf-8'))
                    # server.send('1'.encode())
                conn.close()

    def __accept(self, server):
        try:
            return server.accept()
        except BrokenPipeError:
            return '客户端:%s退出', None
        except Exception as e:
            return e, None

    # def __send(self,server,msg=''):
    #     try:
    #         server.send(msg.)
    def udp_server(self):
        with socket(AF_INET, SOCK_DGRAM) as server:
            server.bind((self.__host, self.__port))
            server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

            while True:
                self.__data, addr = server.recvfrom(self.buffer_size)
                print('接收到客户端：%s 消息' % addr)
                server.sendto(self.__data, addr)


if __name__ == '__main__':
    sc = SocketServer()
    sc.tcp_server()
    # sc.udp_server()
