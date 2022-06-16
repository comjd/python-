from bll import StudentManagerController
from model import StudentModel


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
        age = StudentManagerView.__input_integer('请输入学生年龄：')
        score = StudentManagerView.__input_integer('请输入学生成绩：')
        stu = StudentModel(name, age, score)
        self.__controller.add_student(stu)

    def __update_student(self):
        """
        修改学生信息
        """
        stu_id = StudentManagerView.__input_integer('请输入学生编号：')
        name = input('请输入学生名称：')
        age = StudentManagerView.__input_integer('请输入学生年龄：')
        score = StudentManagerView.__input_integer('请输入学生成绩：')
        stu = StudentModel(name, age, score, stu_id)
        self.__controller.update_student(stu)

    def __remove_student(self):
        """
        删除学生信息
        """
        stu_id = StudentManagerView.__input_integer('请输入学生编号：')
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

    @staticmethod
    def __input_integer(message):
        while True:
            try:
                return int(input(message))
            except:
                continue
