class StudentModel:
    """
    学生信息数据模型类
    """

    def __init__(self, name='', age=0, score=0, stu_id=0):
        self.name = name
        self.age = age
        self.score = score
        self.id = stu_id


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


class StudentManagerView:
    """
    学生信息试图类
    """

    def __init__(self):
        self.__controller = StudentManagerController()

    @staticmethod
    def __print_menu_list():
        print('1)添加学生信息')
        print('2)显示学生信息')
        print('3)修改学生信息')
        print('4)删除学生信息')
        print('5)根据学生信息排序')

    def __select_menu_info(self):
        input_number = input('请输入：')
        if input_number == '1':
            self.__add_student()
        elif input_number == '2':
            self.print_student_info()
        elif input_number == '3':
            self.__update_student()
        elif input_number == '4':
            self.__remove_student()
        elif input_number == '5':
            self.__order_by_student_score()

    def main(self):
        """
        入口
        :return:
        """
        while True:
            self.__print_menu_list()
            self.__select_menu_info()

    def __add_student(self):
        """
        添加学生信息
        """
        name = input('请输入学生名称：')
        age = int(input('请输入学生年龄：'))
        score = int(input('请输入学生成绩：'))
        stu = StudentModel(name, age, score)
        self.__controller.add_student(stu)

    def __update_student(self):
        """
        修改学生信息
        """
        stu_id = int(input('请输入学生编号：'))
        name = input('请输入学生名称：')
        age = int(input('请输入学生年龄：'))
        score = int(input('请输入学生成绩：'))
        stu = StudentModel(name, age, score, stu_id)
        self.__controller.update_student(stu)

    def __remove_student(self):
        """
        删除学生信息
        """
        stu_id = int(input('请输入学生编号：'))
        self.__controller.remove_student(stu_id)

    def __order_by_student_score(self):
        """
        根据学生成绩排序
        """
        for item in self.__controller.order_by_score():
            print('学生id：%d，学生姓名：%s，学生年龄：%d，学生成绩：%d' % (item.id, item.name, item.age, item.score))

    def print_student_info(self):
        """
        打印所有学生信息
        """
        for item in self.__controller.list_student:
            print('学生id：%d，学生姓名：%s，学生年龄：%d，学生成绩：%d' % (item.id, item.name, item.age, item.score))


# controller = StudentManagerController()
# controller.add_student(StudentModel('悟空', 23, 96))
# controller.add_student(StudentModel('八戒', 32, 65))
# controller.add_student(StudentModel('沙僧', 34, 88))
# controller.add_student(StudentModel('唐僧', 44, 100))
# for item in controller.list_student:
#     print(item.id, item.name, item.score)
# # if controller.remove_student(1000):
# #     print('删除成功')
# # else:
# #     print('删除失败')
# controller.update_student(StudentModel('猪八戒', 23, 45, 1001))

# for item in controller.list_student:
#     print(item.id, item.name, item.age, item.score)
# print('------------------')
# for item in controller.order_by_score(False):
#     print(item.id, item.name, item.age, item.score)
# print('------------------')
# for item in controller.list_student:
#     print(item.id, item.name, item.age, item.score)

view = StudentManagerView()
view.main()
view.print_student_info()
