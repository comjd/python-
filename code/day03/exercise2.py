"""
    构建1--50能被５整除的数字,并求和
"""
# # 方式１：
# sum_value = 0
# for item in range(1, 51, 1):
#     if item % 5 == 0:
#         print(item)
#         sum_value += item
# print(sum_value)
# 方式２：
sum_value = 0
for i in range(1, 51, 1):
    if i % 5 != 0:
        continue
    print(i)
    sum_value += i
print(sum_value)
