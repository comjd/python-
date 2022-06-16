"""
封装－－成员数据，类变量，属性
    　　成员方法，类方法，静态方法
"""


class Wife:
    total_number = 0

    def __init__(self, name="", age=18, face_score=0):
        self.name = name
        self.age = age
        self.face_score = face_score
        self.__help_info = '我是只读属性'
        Wife.total_number += 1

    @classmethod
    def get_total_number(cls):
        """
         返回被调用了的次数－－类方法
        :return:
        """
        print('被调用了', cls.total_number)

    @property
    def age(self):
        """
        　get属性
        :return:
        """
        return self.__age

    @age.setter
    def age(self, value):
        """
        set属性－－set属性
        :param value: 年龄
        """
        if 0 <= value <= 120:
            self.__age = value
        else:
            raise Exception('年龄大了啊')

    @property
    def help_info(self):
        """
        只读属性
        :return:
        """
        return self.__help_info

    def set_face_score(self, value):
        """
        颜值的写方法
        :param value:
        """
        if 0 <= value <= 100:
            self.__face_score = value
        else:
            raise Exception('颜值错误')

    # 只写属性的写法
    face_score = property(None, set_face_score)

    @staticmethod
    def print_class():
        print('这个是一个静态方法')


ak = Wife('阿柯', 23, 100)
Wife.get_total_number()
Wife.print_class()
print(ak.help_info)
