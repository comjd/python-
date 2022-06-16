"""
    录入学生的身高，录入空格推出录入

"""
list_height = []
while True:
    height = input('请输入学生的身高，录入空格后结束：')
    if height.strip() == '':
        break
    list_height.append(int(height))
for i in range(len(list_height)):
    print('第', i + 1, '个学生的身高是：', list_height[i])
print('最高身高：', max(list_height))
print('最矮身高：', min(list_height))
print('平均身高：', sum(list_height) / len(list_height))
