"""
    手雷爆炸，玩家受伤（抠血，碎屏），敌人受伤（扣血，头顶冒字）
"""


class Grenade:
    """
    手雷类

    """

    def attack(self, goal):
        """
        爆炸方法
        :param goal: 伤害的目标
        :return:
        """
        goal.damage()


class Goal:
    """
    目标类
    """

    def damage(self):
        print('抠血')


class Player(Goal):
    """
        玩家类，继承目标类
    """

    def damage(self):
        super().damage()
        print('碎屏')


class Enemy(Goal):
    """
        敌人类，继承目标类
    """

    def damage(self):
        super().damage()
        print('头顶冒字')


g01 = Grenade()
p01 = Player()
e01 = Enemy()
g01.attack(p01)
g01.attack(e01)
