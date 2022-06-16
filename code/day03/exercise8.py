"""
    创建列表，存储水星、金星、地球、木星、土星、天王星

"""
start_list = ['水星', '金星', '地球', '木星', '土星', '天王星']
print(start_list)
# 追加
start_list.append('海王星')
print(start_list)
# 在地球后面追加火星
start_list.insert(start_list.index('地球') + 1, '火星')
print(start_list)
print(start_list[-1])
print(start_list[:2])
# 删除金星
start_list.remove('金星')
print(start_list)
start_list[start_list.index('地球') + 1:] = []
print(start_list)
print(start_list[::-1])
