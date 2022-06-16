"""
    10-50间个位不是2,5,9的整数
"""
sum_value = 0
for i in range(9, 51):
    if i % 10 not in (2, 5, 9):
        print(i)
        sum_value += i
print(sum_value)
