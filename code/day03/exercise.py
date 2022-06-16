"""
    输入边长，打印矩形
"""

length = int(input("请输入边长："))
if length <= 2:
    print('边长过短')
# 第一种输入方案
else:
    print('*' * length)
    for i in range(length - 2):
        print('*' + ' ' * (length - 2) + '*')
    print('*' * length)
# else:
#     for item in range(length):
#         if item == 0 or item == length - 1:
#             print('*' * length)
#         else:
#             print('*' + '/' * (length - 2) + '*')
