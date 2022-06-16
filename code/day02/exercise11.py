"""
    猜随机数
"""
import random

num = random.randint(1, 100)
print(num)
temp = 0
while temp != num:
    temp = int(input('请输入一个整数(1~100)：'))
    if temp > num:
        print('猜大了')
    elif temp < num:
        print('猜小了')
    else:
        print('猜对了')
        if input('输入1可以再玩一次') == '1':
            num = random.randint(1, 100)
            temp = 0
            print(num)
        else:
            print('游戏退出')
            break
