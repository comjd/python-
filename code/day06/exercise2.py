"""
老婆类
"""


class Wife:
    def __init__(self, name='', age=0, face_score=0):
        self.name = name
        self.age = age
        self.face_score = face_score

    def get_all_wife(self):
        return [
            Wife('阿科', 23, 90),
            Wife('苏荃', 32, 80),
            Wife('双儿', 21, 85),
            Wife('公主', 25, 95),
            Wife('丫鬟', 18, 67),
            Wife('小敏', 19, 70),
        ]

    def print_all_info(self):
        print(self.name, self.face_score, self.age)

    def get_all_name(self):
        return [item.name for item in self.get_all_wife()]

    def get_face_score_80(self):
        """
        颜值高于80分的人数
        :return:
        """
        return [item for item in self.get_all_wife() if item.face_score >= 80]

    def get_max_age(self):
        """
        年龄最大的老婆
        :return:
        """
        max_age = self.get_all_wife()[0]
        for item in self.get_all_wife():
            if max_age.age < item.age:
                max_age = item
        return max_age

    def order_asc_face_score(self):
        """
        年龄升序
        :return:
        """
        all_wife = self.get_all_wife()
        for i in range(len(all_wife)-1):
            for j in range(i + 1, len(all_wife)):
                if all_wife[i].face_score > all_wife[j].face_score:
                    all_wife[i], all_wife[j] = all_wife[j], all_wife[i]
        return all_wife


wife1 = Wife()
for item in wife1.order_asc_face_score():
    item.print_all_info()
