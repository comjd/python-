from socket import *


class TcpClient:
    def __init__(self, ip, port):
        self.__client = socket(AF_INET, SOCK_STREAM, 0)
        self.__server_addr = (ip, port)
        self.data = ''

    def create_client(self):
        is_success = self.__client_connect()
        if is_success:
            print(is_success)
        else:
            while True:
                self.__client.send(self.data.encode())
                if not self.data:
                    break
                self.__client_recv()

    def __client_connect(self):
        try:
            self.__client.connect(self.__server_addr)
        except ConnectionRefusedError:
            return '连接失败'
        except Exception as e:
            return e

    def __client_recv(self):
        self.data = self.__client.recv(1024)
        return self.data

    def send_msg(self, msg=''):
        self.data = msg


if __name__ == '__main__':
    c = TcpClient('127.0.１.1', 8080)
    c.create_client()

    while True:
        file = input('上传文件：')
        if file == 'q':
            c.send_msg()
            break
        if not file:
            file = '/home/tyler/图片/1.jpeg'
        with open(file, 'rb') as rd:
            for line in rd:
                print(line)
                c.send_msg(line)
