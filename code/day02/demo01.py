"""
    逻辑结果
"""
re = 1 > 2 and input("请输入a") == 'a'
print(re)

re = 2 > 1 or input("请输入a") == 'a'
print(re)

re = 2 > 1 and input("请输入a：") == 'a'
print(re)
