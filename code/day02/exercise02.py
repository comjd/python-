"""
    输入数字后，计算各个数字相加的和,暂时只支持４位数据字
"""
str_number = int(input('请输入4位整数：'))
result = 0
result = str_number % 10 + str_number // 10 % 10 + str_number // 10 // 10 % 10 + str_number // 1000

print(result)
