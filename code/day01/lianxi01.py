def calculate(amount=100, money=100, gj=5, mj=3, xj=1 / 3):
    """
    百钱百鸡　使用的算法是[枚举类]
    :param amount: 总数,默认值100
    :param money: 花费的钱,默认值100
    :param gj: 公鸡单价,默认值5
    :param mj: 母鸡单价,默认值3
    :param xj: 小鸡单价,默认值1/3
    :return: 返回满足条件的公鸡、母鸡、小鸡各多少只的list
    """
    lists = []
    for i in range(0, int(money / gj + 1)):
        for j in range(0, int(money / mj + 1)):
            for y in range(0, int(money / xj + 1)):
                if (i + j + y) == amount and (i * gj + j * mj + y * xj) == 100:
                    lists.append([i, j, y])
                    print('公鸡%d只，母鸡%d只，小鸡%d只' % (i, j, y))
    if not lists:
        print('无解了')
    return lists


print(calculate(100, 300, xj=1 / 2))
