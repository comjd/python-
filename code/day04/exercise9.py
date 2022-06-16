"""
    将２个列表合并为字典(使用的字典推导式)
"""
list01 = ['李四', '王丽', '张望', '李小龙']
list02 = [101, 102, 103, 104]
dict01 = {list01[i]: list02[i] for i in range(len(list01))}
print(dict01)