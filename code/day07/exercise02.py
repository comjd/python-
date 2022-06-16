class Person:
    def __init__(self, name=""):
        self.name = name

    def teach(self, person, skill):
        print(self.name, '教', person.name, skill)

    def work(self, money):
        print(self.name, '上班挣了', money, '元钱')


p01 = Person('张无忌')
p02 = Person('赵敏')

p01.teach(p02, '九阳神功')
p02.teach(p01, '化妆')
p01.work(10000)
p02.work(8000)
