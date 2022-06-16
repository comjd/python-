class StudentManagerController:
    """
    学生信息控制类
    """

    init_id = 1000

    def __init__(self):
        self.__list_student = []

    @classmethod
    def __get_student_id(cls, stu):
        """
        获取学生id
        :param stu: 学生信息
        """
        stu.id = cls.init_id
        cls.init_id += 1

    @property
    def list_student(self):
        """
        获取学生列表信息
        :return: 返回学生信息列表
        """
        return self.__list_student

    def add_student(self, stu):
        """
        添加学生信息
        :param stu: 学生信息
        :return: 添加是否成功
        """
        StudentManagerController.__get_student_id(stu)
        if not self.check_student_exist(stu):
            self.__list_student.append(stu)
            return True
        return False

    def check_student_exist(self, stu):
        """
        检查学生id是否存在
        :param stu: 学生信息
        :return: 学生信息是否存在
        """
        for student in self.__list_student:
            if student.id == stu.id:
                return True
        return False

    def remove_student(self, stu_id):
        """
        删除学校信息
        :param stu_id:学生id
        :return: 是否删除成功
        """
        for student in self.__list_student:
            if student.id == stu_id:
                self.__list_student.remove(student)
                return True
        return False

    def update_student(self, new_stu):
        """
        修改学生信息
        :param new_stu:学生信息
        :return: 修改是否成功
        """
        for student in self.__list_student:
            if student.id == new_stu.id:
                student.name = new_stu.name
                student.age = new_stu.age
                student.score = new_stu.score
                return True
        return False

    def order_by_score(self, asc=True):
        """
        按照学生分数排序
        :param asc: True顺序，False倒序
        :return: 排序后的列表
        """
        list_stu = self.__list_student[::]
        for i in range(len(list_stu) - 1):
            for j in range(i + 1, len(list_stu)):
                if list_stu[i].score >= list_stu[j].score and asc:
                    list_stu[i], list_stu[j] = list_stu[j], list_stu[i]
                    continue
                elif list_stu[i].score < list_stu[j].score and not asc:
                    list_stu[i], list_stu[j] = list_stu[j], list_stu[i]
        return list_stu
