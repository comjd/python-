"""
    根据输入的秒数，转换成几时几分几秒
"""

input_second = int(input("请输入总的秒数："))
secode = input_second % 60
minute = input_second // 60 % 60
hour = input_second // 60 // 60 % 24
day = input_second // 60 // 60 // 24
print(input_second, '秒换算后的结果为：', day, '天零', hour, '小时零', minute, '分钟零', secode, '秒')
