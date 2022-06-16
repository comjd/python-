"""
    在控制台输入日期（月日），输出日期是这一年的第多少天
"""
day = input('请输入日期(例如：3月15日)：')
tuple_days = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
month = int(day[:(day.find('月'))])
days = int(day[(day.find('月')) + 1:(day.find('日'))])
print(sum(tuple_days[:month-1]) + days)
