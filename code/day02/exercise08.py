"""
    １、请一个整数判断奇数偶数；
    ２、输入年份润年２９非润年２８
"""
# print('奇数' if int(input('请输入一个整数：')) % 2 else '偶数')
year = int(input('请输入一个年份：'))
print('29' if not year % 4 and year % 100 or not year % 400 else '28')
