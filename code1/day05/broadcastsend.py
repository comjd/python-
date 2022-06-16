"""
    广播消息发送端
"""
import time
from socket import *

data = """
*************
地点：成都
温度：38.6
时间：%s
*************
    """
s = socket(AF_INET, SOCK_DGRAM, 0)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
while True:
    time.sleep(2)
    s.sendto(str(data % time.ctime()).encode(), ('192.168.10.255', 8899))
