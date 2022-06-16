"""
　2048游戏
"""

list_merger = [2, 0, 0, 2]


def zero_to_end():
    """
    将非0数字移动到末尾
    :return:
    """
    for item in range(len(list_merger) - 1, -1, -1):
        if list_merger[item] == 0:
            del list_merger[item]
            list_merger.append(0)


def merger():
    """
    合并相邻且相同的数据
    :return:
    """
    zero_to_end()
    for item in range(len(list_merger) - 1):
        if list_merger[item] == list_merger[item + 1]:
            list_merger[item] += list_merger[item + 1]
            del list_merger[item + 1]
            list_merger.append(0)


number_map = [
    [2, 0, 0, 2],
    [2, 4, 4, 2],
    [0, 4, 2, 0],
    [2, 0, 2, 0]
]


def move_left():
    """
    向左移动
    """
    global list_merger
    for line in number_map:
        list_merger = line
        merger()


def move_right():
    """
    向右移动
    """
    global list_merger
    for line in number_map:
        list_merger = line[::-1]
        merger()
        line[::-1] = list_merger


def founder_transpose():
    """
    方正转置
    :return:
    """
    for i in range(len(number_map) - 1):
        for j in range(i + 1, len(number_map)):
            number_map[i][j], number_map[j][i] = number_map[j][i], number_map[i][j]


def move_up():
    """
    向上移动
    """
    founder_transpose()
    move_left()
    founder_transpose()


def move_down():
    """
    向下移动
    """
    founder_transpose()
    move_right()
    founder_transpose()



move_down()
print(number_map)
