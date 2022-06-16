"""
    判断输入的数字是否为素数
"""
in_number = int(input('请输入整数：'))
for i in range(2, in_number):
    if in_number % i == 0:
        print('不是素数')
        break
else:
    print('%d是素数' % in_number)
