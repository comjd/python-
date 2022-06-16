"""
    在控制台中循环输入内容，输入空退出循环
    输入不重复的结果
"""
set01=set()
while True:
    input_str = input('请输入内容')
    if input_str=="":
        break
    set01.add(input_str)
print(set01)
