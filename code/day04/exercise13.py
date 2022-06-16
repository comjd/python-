"""
    方正转置
"""
list01 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]
for i in range(len(list01) - 1):
    for j in range(i + 1, len(list01)):
        list01[i][j], list01[j][i] = list01[j][i], list01[i][j]
print(list01)
