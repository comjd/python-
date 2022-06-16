"""
    计算字符串中每个字符出现次数。
    输入：abcb...
    输出：字符a,2次
"""

input_str = input('请输入字母字符串')
char_of_numbers = {}
for i in input_str:
    if i in char_of_numbers:
        char_of_numbers[i] = char_of_numbers[i] + 1
    else:
        char_of_numbers[i] = 1
for k, v in char_of_numbers.items():
    print(k, v)
