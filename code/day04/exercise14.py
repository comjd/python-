"""
    一元二次方程求解
"""


def quadratic(a, b, c, d=0):
    """
    一元二次方程求解
    :param a: 第1个数，int类型
    :param b: 第2个数，int类型
    :param c: 第3个数，int类型
    :param d: 第2个数，int类型 ，默认为0
    :return:  计算结果
    """

    import math
    for i in [a, b, c, d]:
        if not isinstance(i, (int, float)):
            return '参数错误'
    if d >= 0:
        c -= d
    else:
        c += abs(d)
    temp = b ** 2 - 4 * a * c
    if a == 0:
        return 'a不能等于０'
    if temp > 0:
        result1 = (-b + math.sqrt(temp)) / (2 * a)
        result2 = (-b - math.sqrt(temp)) / (2 * a)
        return result1, result2
    elif temp == 0:
        return (-b) / (2 * a)
    else:
        return '无解'


print(quadratic(2, 3, 0, -1))
print(quadratic(1, 3, -5,-1))
print(quadratic(0.1, 0, -4, 0))
print(quadratic(1, 3, -4, 'a'))
# 9-(4*1*(-9))
