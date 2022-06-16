"""
    一张纸的厚度为0.01毫米，对折多少次超过8844.33米
"""
height = 0.01
count = 0
while height < 8844.33*10**3:
    height *= 2
    print(count, '次', height, '毫米')
    count += 1
else:
    print(count)
