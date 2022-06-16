import time
from socket import *


def server():
    tcp_server = socket()
    tcp_server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    tcp_server.bind(('0.0.0.0', 8080))
    tcp_server.listen(5)
    while True:
        print('waiting...')
        conn, addr = tcp_server.accept()
        print('connect from ', addr)
        f = open('2.jpeg', 'wb')
        while True:
            data = conn.recv(100)
            if not data:
                print('0000')
                break
            print(data.decode())
            # f.write(data)
            # f.flush()
            # if not data or data == '\r\n':
            #     break
            # print('client info:', data.decode())
            #
            # # write(time.time(), data)
            # print(data.decode())
            # conn.send('1'.encode())
            # print('00000')
        conn.send('1'.encode())
        f.close()
        conn.close()
    tcp_server.close()


def writefile(func):
    def warp(*args, **kwargs):
        func(args, kwargs)

    return warp


def write(name, data):
    with open(name, 'wb'):
        pass
    with open(name, 'ab') as wf:
        while data is None:
            wf.write(data)


if __name__ == '__main__':
    server()
