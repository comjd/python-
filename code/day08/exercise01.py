class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __iadd__(self, other):
        """
        重写+=
        重写__iadd__实现向量坐标的x,y直接相加, 不会生成新的对象
        :param other:
        :return:
        """
        self.x += other.x
        self.y += other.y
        return self

    def __add__(self, other):
        """
        重写+
        重写__add__实现向量坐标的x,y直接相加, 会生成新的对象
        :param other:
        :return:
        """
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        """
        重写__str__
        :return:
        """
        return "Vector x：%d，y:%d" % (self.x, self.y)

    def __repr__(self):
        """
        重写__str__
        :return:
        """
        return "Vector(%d,%d)" % (self.x, self.y)

    def __lt__(self, other):
        """
        重写 <
        :param other:比较的对象
        :return:
        """
        if self.x + self.y < other.x + other.y:
            return True
        return False

    def __eq__(self, other):
        """
        重写比较
        :param other:比较的对象
        :return:
        """
        if self.x + self.y < other.x + other.y:
            return True
        return False


v01 = Vector(1, 2)
print(v01)
v02 = Vector(0, 2)
v01 += v02
print(v01)
# 利用eval()实现类拷贝
v03 = eval(v01.__repr__())
v01.x = 10
print(v03)
print(v01)

print(v01 < v03)

list01 = [v01, v02, v03]
print(sorted(list01))
