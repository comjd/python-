from socket import *


def client():
    tcp_client = socket()
    tcp_client.connect(('127.0.0.1', 8080))
    f = open('/home/tyler/图片/1.jpeg', 'rb')
    while True:
        # data = f.read(100)
        data = input('>>')
        if not data:
            print('---------------')
            break
        tcp_client.send(data.encode())
        # tcp_client.send(data)
    result = tcp_client.recv(100)
    print(result.decode())
    # if result == '1':
    #     print('success')
    tcp_client.close()


if __name__ == '__main__':
    client()
