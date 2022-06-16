"""
    输入：　How are you　后　反转

"""
str_temp = input('请收入How are you：')
list_temp = str_temp.split(' ')
print(" ".join(list_temp[::-1]))
