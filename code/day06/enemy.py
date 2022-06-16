class Enemy:
    def __init__(self, hp=0, atk=0, mp=100):
        self.hp = hp
        self.atk = atk
        self.__arms = '匕首'  # 只读属性
        self.mp = mp  # 只写属性

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        if 0 <= value <= 50:
            self.__hp = value
        else:
            raise Exception('血量超标了')

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        if 1 <= value <= 100:
            self.__atk = value
        else:
            raise Exception('攻击力异常')

    @property
    def arms(self):
        return self.__arms

    def mp(self, value):
        if 0 <= value <= 200:
            print(value)
            self.__mp = value
        else:
            raise Exception('魔法值错误了')

    mp = property(None, mp)

    def print_class(self):
        print('生命力：', self.hp, '攻击力：', self.atk)


e1 = Enemy(30, 20)
e1.print_class()
print(e1.arms)
e1.mp = 200
