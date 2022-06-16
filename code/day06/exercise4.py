"""
    静态方法
"""


class Vector:
    """
    向量
    """

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @staticmethod
    def move_right():
        """
        向右移动
        :return: 返回Vector(0, 1)
        """
        return Vector(0, 1)

    @staticmethod
    def move_left():
        """
        向左移动
        :return: 返回Vector(0, -1)
        """
        return Vector(0, -1)

    @staticmethod
    def move_up():
        """
        向上移动
        :return: 返回Vector(-1, 0)
        """
        return Vector(-1, 0)

    @staticmethod
    def move_down():
        """
        向下移动
        :return: 返回Vector(1, 0)
        """
        return Vector(1, 0)


class DoubleListHelper:
    """
    二维列表助手列表类
    """

    @staticmethod
    def get_elements(list_target, vect_tops, vect_dir, count):
        """
        根据指定位置截取指定长度的列表
        :param list_target: 源列表
        :param vect_tops: 开始位置
        :param vect_dir: 移动方向
        :param count: 截取长度
        :return: 截取结果列表
        """

        result_list = []
        for __ in range(count):
            vect_tops.x += vect_dir.x
            vect_tops.y += vect_dir.y
            result_list.append(list_target[vect_tops.x][vect_tops.y])
        return result_list


test_list = [[str(i) + str(j) for j in range(10)] for i in range(10)]
print(test_list)
print(DoubleListHelper.get_elements(test_list, Vector(2, 1), Vector.move_right(), 6))
print(DoubleListHelper.get_elements(test_list, Vector(5, 9), Vector.move_left(), 6)[::-1])
print(DoubleListHelper.get_elements(test_list, Vector(9, 9), Vector.move_up(), 9)[::-1])
print(DoubleListHelper.get_elements(test_list, Vector(0, 2), Vector.move_down(), 9))
