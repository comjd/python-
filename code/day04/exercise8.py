"""
    在控制台中录入人的姓名及他的多个爱好，姓名为空时退出录入
    输出所有人的名称及基本信息
"""
person_list = {}
while True:
    name = input('请输入姓名：')
    if name == "":
        break
    person_list[name] = []
    while True:
        like = input('请输入' + name + '的爱好：')
        if like == "":
            break
        person_list[name].append(like)
for k, v in person_list.items():
    print(k, ",".join(v))
