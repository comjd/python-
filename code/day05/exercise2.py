"""
    根据小时、分钟、秒数计算总秒数
"""


def get_total_seconds(hour=0, minute=0, second=0):
    return hour * 60 ** 2 + minute * 60 + second


print(get_total_seconds(1, 1, 1))
