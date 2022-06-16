# -*- coding: utf-8 -*-
# @Time : 2022/5/15 下午7:41
# @Author : tyler
# @File : pool.py
# @Project : code1

from multiprocessing import Pool
from time import sleep, ctime


def worker(msg):
    sleep(2)
    print(msg + '---' + ctime())


# 初始化4个进程池
p = Pool(2)
for i in range(1, 11):
    # 　通过apply_async注册进程池
    p.apply_async(func=worker, args=('process ' + str(i),))

# 关闭进程池
p.close()
# 回收进程池
p.join()

if __name__ == '__main__':
    pass
