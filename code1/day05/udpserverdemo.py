import time
from socket import *


def server():
    udp_server = socket(AF_INET, SOCK_DGRAM, 0)
    udp_server.bind(('0.0.0.0', 9090))
    while True:
        time.sleep(1)
        data, addr = udp_server.recvfrom(1024)
        print(addr)
        udp_server.sendto(time.ctime().encode(), addr)


if __name__ == '__main__':
    server()
