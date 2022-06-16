"""
    从输入的数字中找出最大值
"""
a = int(input("请输入地1个数字："))
b = int(input("请输入地1个数字："))
c = int(input("请输入地1个数字："))
d = int(input("请输入地1个数字："))
if a < b:
    a = b
if a < c:
    a = c
if a < d:
    a = d
print(a)
