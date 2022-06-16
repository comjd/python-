"""
    老张开车去东北
"""


class Person:
    def __init__(self, name=''):
        self.name = name

    def go_to(self, traffic):
        print('走了')
        traffic.run()


class Traffic:

    def run(self):
        pass


class Car(Traffic):
    def run(self):
        super().run()
        print('嘟嘟~')


class Airplane(Traffic):
    def run(self):
        super().run()
        print('起飞了～')


lz = Person('老张')
c01 = Car()
a01 = Airplane()

lz.go_to(c01)
lz.go_to(a01)
