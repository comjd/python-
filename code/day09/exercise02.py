class Skill:

    def __init__(self, data=None):
        self.__data = data
        self.__count = -1

    def __next__(self):
        self.__count += 1
        if self.__count <= len(self.__data) - 1:
            return self.__data[self.__count]
        else:
            raise StopIteration()


class SkillManager:
    def __init__(self):
        self.__skills = []

    def add_skill(self, skill):
        self.__skills.append(skill)

    def __iter__(self):
        return Skill(self.__skills)


sm = SkillManager()
sm.add_skill('悟空')
sm.add_skill('八戒')
sm.add_skill('唐山')
iterator = sm.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break
