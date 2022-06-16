# -*- coding: utf-8 -*-
# @Time : 2022/5/13 下午9:19
# @Author : tyler
# @File : fork01.py
# @Project : code1

"""
    生成一个子进程
"""
import os

# 只有原进程执行一次
print('=============')

# 赋值语句在原进程会执行，但是新的进程会把原进程的内存中的值全部复制一份
a = 1

# 　创建进程
pid = os.fork()

# 创建进程失败后执行
if pid < 0:
    print('Error')
# 创建的新进程执行
elif pid == 0:
    print('the new process')
# 原进程执行
else:
    print('the old process')

# 所有进程都会执行一次
print('process work over')

if __name__ == '__main__':
    pass
