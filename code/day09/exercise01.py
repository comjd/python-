"""
    异常处理
"""


class Wife:
    def __init__(self, age=0):
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if 20 <= value <= 30:
            self.__age = value
        else:
            raise Exception('我不要')


try:
    w01 = Wife(40)
    print(w01.age)
except Exception as e:
    print(e.args)
