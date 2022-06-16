"""
    一个小球从100米高度落下，每次弹回原高度的一半
    到小球落地(小于0.01)一个跳了多少次，一共运行了多少米
"""
height = 100
cont = 0
juli = height
while height / 2 >= 0.01:
    height /= 2
    cont += 1
    print(cont, '高度：', height)
    juli += height * 2  # 起落距离
print(cont, juli)
