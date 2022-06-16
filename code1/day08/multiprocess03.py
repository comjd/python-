# -*- coding: utf-8 -*-
# @Time : 2022/5/15 下午7:33
# @Author : tyler
# @File : multiprocess03.py
# @Project : code1
import time
from multiprocessing import Process


def worker():
    for i in range(2):
        time.sleep(2)
        print('子进程工作。。。')


p = Process(target=worker())
p.daemon = True  # 守护线程，开启后主进程结束后，子进程会全部退出
print(p.name)
p.start()
print(p.pid)
print('是否存活，需要在start后为Ｔrue:', p.is_alive())

p.join()

if __name__ == '__main__':
    pass
