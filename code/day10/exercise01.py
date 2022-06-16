from day10.iterator_tools import IterableHelper


class Wife:
    def __init__(self, name='', age=0, face_score=0, height=0):
        self.name = name
        self.age = age
        self.face_score = face_score
        self.height = height

    def __str__(self):
        return "%s,%d,%d,%d," % (self.name, self.age, self.face_score, self.height)


list01 = [
    Wife('悟空', 23, 67, 170),
    Wife('八戒', 24, 57, 165),
    Wife('唐僧', 25, 98, 172),
    Wife('如来', 45, 71, 182),
    Wife('玉帝', 56, 87, 165),
    Wife('观音菩萨', 21, 89, 158),
    Wife('小白龙', 28, 88, 173),
]


def select_all_name():
    for item in list01:
        yield item.name


# for item in select_all_name():
#     print(item)


# def func01():
#     for item in list01:
#         if condition01(item):
#             yield item
#
#
# def func02():
#     for item in list01:
#         if condition02(item):
#             yield item


# def condition01(item):
#     return item.age > 25
#
#
# def condition02(item):
#     return item.face_score > 25


# for item in func01():
#     print(item)
#
# print('---------------')
# for item in func02():
#     print(item)

# for item in IteratorHelper().find_all(list01, condition01):
#     print(item)
#
# print('---------------')
# for item in IteratorHelper().find_all(list01, condition02):
#     print(item)


def condition01(max, item):
    return item.age > max.age


def condition02(item):
    return item.face_score > 25


print(IterableHelper.get_max(list01, lambda item: item.age))  # 年龄最大的元素
print(IterableHelper.get_max(list01, lambda item: item.face_score))  # 颜值最高的元素
print(IterableHelper.get_max(list01, lambda item: item.height))  # 身高最高的元素
print(IterableHelper.sum(list01, lambda item: item.height))  # 身高求和
print(IterableHelper.sum(list01, lambda item: item.face_score))  # 颜值求和
print(IterableHelper.is_exist(list01, lambda item: item.name == '悟空'))  # 是否存在名字为悟空的对象
print(IterableHelper.is_exist(list01, lambda item: item.face_score > 98))  # 是否存在颜值高于98的对象
