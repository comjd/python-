"""
    风清扬使用独孤九剑攻击
    任我行使用吸星大法攻击
    令狐冲使用独孤九剑和吸星大法攻击
    ...
    可能还有更多人和更多技能
"""


class Person:
    def __init__(self, name=''):
        self.name = name
        self.__list_skill = []

    def add_skill(self, skill):
        self.__list_skill.append(skill)

    def use_skill(self):
        for item in self.__list_skill:
            print(self.name, item.attack())


class Skill:
    def __init__(self, name=''):
        self.name = name

    def attack(self):
        return self.name + '攻击'


class Dugujiujian(Skill):
    def __init__(self, name=''):
        super().__init__(name)

    def attack(self):
        return super().attack()


class Xixingdafa(Skill):
    def __init__(self, name=''):
        super().__init__(name)

    def attack(self):
        return super().attack()


class Kuihuabaodian(Skill):
    def __init__(self, name=''):
        super().__init__(name)

    def attack(self):
        return super().attack()


fqy = Person('风清扬')
rwx = Person('任我行')
lhc = Person('令狐冲')
dgjj = Dugujiujian('独孤九剑')
xxdf = Xixingdafa('吸星大法')
khbd = Kuihuabaodian('葵花宝典')

fqy.add_skill(dgjj)
rwx.add_skill(xxdf)
lhc.add_skill(dgjj)
lhc.add_skill(xxdf)
lhc.add_skill(khbd)

fqy.use_skill()
rwx.use_skill()
lhc.use_skill()
