"""
    tpc_scorct_server demo
"""
import time
from socket import *


class TcpSocket:
    def __init__(self, ip='0.0.0.0', port=8080):
        # 　创建套接字
        self.__server = socket(AF_INET, SOCK_STREAM, 0)
        self.__addr = (ip, port)
        self.__conn = None
        self.data = ''

    def create_server(self):
        """
            创建套接字服务端
        :return:
        """
        self.__create_init()
        while True:
            self.__conn, addr = self.__socket_accept()
            if addr is None:
                print(self.__conn)
                break
            while True:
                data = TcpSocket.__socket_recv(self.__conn)
                if not data:
                    print(addr, '已断开！')
                    break
                print('收到客户端消息：', data.decode())
                time.sleep(4)
                self.send_msg()
            TcpSocket.close(self.__conn)
        TcpSocket.close(self.__server)

    def __create_init(self):
        # 　服务端结束后是否立即释放端口
        self.__server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        # 绑定服务端的ip和端口
        self.__server.bind(self.__addr)
        # 设置监听数量，
        self.__server.listen(5)

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

    @staticmethod
    def __socket_recv(conn):
        """
        接收消息
        :param conn: 客户端套接字对象
        :return: 接收到的信息内容
        """
        # 收到消息的缓冲区大小
        data = conn.recv(1024)
        if not data and data == '\r\n':
            return None
        return data

    def send_msg(self, msg='y'):
        """
            发送消息
        :param conn: 客户端套接字对象
        :param msg: 需要发送消息的内容
        :return:
        """
        self.__conn.send(msg.encode())

    @staticmethod
    def close(arg_socket):
        arg_socket.close()


if __name__ == '__main__':
    ts = TcpSocket()
    ts.create_server()
    # ts.send_msg('no')
