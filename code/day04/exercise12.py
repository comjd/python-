"""
    对列表进行排序，
"""
list01 = [1, 8, 9, 21, 0]
#
# for item in range(len(list01) - 1):
#     for j in range(item + 1, len(list01)):
#         if list01[item] > list01[j]:
#             list01[item], list01[j] = list01[j], list01[item]
# print(list01)
for i in range(len(list01) - 1):
    for j in range(i + 1, len(list01)):
        if list01[i] < list01[j]:
            list01[i], list01[j] = list01[j], list01[i]
print(list01)