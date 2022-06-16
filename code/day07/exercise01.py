"""
需求：玩家攻击敌人
"""


class Player:
    def __init__(self, atk=0):
        self.atk = atk

    def to_atk(self, target):
        print('攻击')
        target.injured(self.atk)


class Enemy:
    def __init__(self, hp=0):
        self.hp = hp

    def injured(self, value):
        self.hp -= value
        print('啊')
        if self.hp <= 0:
            self.death()

    def death(self):
        print('死咯')


p01 = Player(50)
e01 = Enemy(100)
p01.to_atk(e01)
p01.to_atk(e01)
