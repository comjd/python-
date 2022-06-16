class Dog:
    """
    狗类
    """

    def __init__(self, variety, nickname, age, sex):
        self.variety = variety
        self.nickname = nickname
        self.age = age
        self.sex = sex

    def eat(self):
        print(self.nickname, '肯骨头')


dog01 = Dog('阿拉斯加', '大白', 3, '公')
dog02 = Dog('二哈', '毛毛', 2, '母')
dog01.eat()
dog02.eat()
