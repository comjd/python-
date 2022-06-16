import random

from locationmodel import LocationModel


class GameCoreController:
    def __init__(self):
        self.__list_merger = None
        self.__map = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.__list_empty = []

    @property
    def map(self):
        return self.__map

    def zero_to_end(self):
        """
        将非0数字移动到末尾
        :return:
        """
        for item in range(len(self.__list_merger) - 1, -1, -1):
            if self.__list_merger[item] == 0:
                del self.__list_merger[item]
                self.__list_merger.append(0)

    def merger(self):
        """
        合并相邻且相同的数据
        :return:
        """
        self.zero_to_end()
        for item in range(len(self.__list_merger) - 1):
            if self.__list_merger[item] == self.__list_merger[item + 1]:
                self.__list_merger[item] += self.__list_merger[item + 1]
                del self.__list_merger[item + 1]
                self.__list_merger.append(0)

    def move_left(self):
        """
        向左移动
        """

        for line in self.map:
            self.__list_merger = line
            self.merger()

    def move_right(self):
        """
        向右移动
        """
        for line in self.map:
            self.__list_merger = line[::-1]
            self.merger()
            line[::-1] = self.__list_merger

    def founder_transpose(self):
        """
        方正转置
        :return:
        """
        for i in range(len(self.map) - 1):
            for j in range(i + 1, len(self.map)):
                self.map[i][j], self.map[j][i] = self.map[j][i], self.map[i][j]

    def move_up(self):
        """
        向上移动
        """
        self.founder_transpose()
        self.move_left()
        self.founder_transpose()

    def move_down(self):
        """
        向下移动
        """
        self.founder_transpose()
        self.move_right()
        self.founder_transpose()

    def generate_new_number(self):
        """
            生成一个新的随机数
        """
        self.__get_all_zero_location()
        if len(self.__list_empty) == 0:
            return
        loc = random.choice(self.__list_empty)
        self.__map[loc.x][loc.y] = self.__get_random_number()

    def __get_random_number(self):
        """
        按照10%的概率生成4，按照90%的概率生成2
        :return: 返回2或者4
        """
        return 4 if random.randint(1, 10) == 1 else 2

    def __get_all_zero_location(self):
        """
        获取所有0的位置
        :return: 返回所有0元素的位置列表
        """
        self.__list_empty.clear()
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if self.map[i][j] == 0:
                    self.__list_empty.append(LocationModel(i, j))

    def game_over(self):
        """
        游戏是否结束
        :return: True游戏结束,False游戏继续
        """
        if len(self.__list_empty) > 0:
            return False
        for i in range(len(self.map) - 1):
            for j in range(len(self.map[i]) - 1):
                if self.map[i][j] == [i + 1][j] or self.map[j][i] == self.map[j + 1][i]:
                    return False
        return True


if __name__ == '__main__':
    """
    测试代码
    """
    ctrl = GameCoreController()
    ctrl.generate_new_number()
    ctrl.generate_new_number()
    ctrl.move_left()
    print(ctrl.map)
