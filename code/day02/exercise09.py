"""
　　　 根据输入的开始数字和结束数字　输出中间的数字
"""

start_number = int(input('请输入数字：'))
end_number = int(input('请输入数字：'))
# if start_number > end_number:
#     start_number, end_number = end_number, start_number
# while start_number < end_number-1:
#     start_number += 1
#     print(start_number)

direction = 1 if start_number < end_number else -1
if start_number == end_number:
    print(start_number)
else:
    while start_number != end_number - direction:
        start_number += direction
        print(start_number)
