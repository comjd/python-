from socket import *


def client():
    udp_client = socket(AF_INET, SOCK_DGRAM, 0)
    server_addr = ('127.0.0.1', 9090)
    while True:
        udp_client.sendto('123'.encode(), server_addr)
        msg, addr = udp_client.recvfrom(1024)
        print(msg.decode())


if __name__ == '__main__':
    client()
