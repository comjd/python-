"""
    1.使用生成器表达式找出列表中的字符串
    2.使用生成器表达式找出列表中的大于10的整数
"""
list01 = ['无可', 99, '就空间', "jfkdja", True, 6.88, '金卡就', 90, 10, 9.08, 100.00]

for item in (i for i in list01 if isinstance(i, str)):
    print(item)
print('--------------')
for item in (i for i in list01 if isinstance(i, int) and i > 10):
    print(item)
