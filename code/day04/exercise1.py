"""
    通过终端输入内容，拼接打印出来
"""
list_temp = []
while True:
    str_item = input('请输入内容：')
    if str_item.strip() == '':
        break
    list_temp.append(str_item)
print(''.join(list_temp))
