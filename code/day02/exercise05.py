"""
    输入２个数字和一个运算符，并输出结果
"""
a = float(input('请输入１个数字:'))
f = input('请输入１个符号:')
if f in ('*', '+', '-', '/'):
    b = float(input('请再输入１个数字:'))
    if f == '*':
        print(a * b)
    elif f == '+':
        print(a + b)
    elif f == '-':
        print(a - b)
    elif f == '/':
        print(a / b)
else:
    print('符号输入错误')
