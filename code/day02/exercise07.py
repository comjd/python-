"""
    根据月份输入对应的天数
"""
month = int(input('请输入月份：'))
if month > 12 or month < 1:
    print('月份输入错误')
elif month == 2:
    print(28)
elif month in (1, 3, 5, 7, 8, 10, 12):
    print(31)
else:
    print(30)
