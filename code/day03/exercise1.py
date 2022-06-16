"""
    循环累加下列数字的和 0,1,2,3,4,5
    循环累加下列数字的和 2,3,4,5,6,7
    循环累加下列数字的和 0,2,4,6
    循环累加下列数字的和 4,3,2,1,0
    循环累加下列数字的和 -1,-2,-3,-4
"""
result = 0
for i in range(6):
    print(i)
    result += i
print(result)

result = 0
for i in range(2, 8):
    print(i)
    result += i
print(result)

result = 0
for i in range(0, 7, 2):
    print(i)
    result += i
print(result)

result = 0
for i in range(4, -1, -1):
    print(i)
    result += i
print(result)

result = 0
for i in range(-1, -5, -1):
    print(i)
    result += i
print(result)
