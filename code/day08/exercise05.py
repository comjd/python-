"""
    创建员工管理器：
        1.记录所有员工
        2.计算总薪水
    岗位:
        1.程序员：底薪＋项目分红
        2.测试员：底新＋Bug数*5
"""


class EmployeesManager:
    def __init__(self):
        self.__list_employees = []

    def get_list_employees(self):
        return self.__list_employees

    def add_employees(self, employees):
        self.__list_employees.append(employees)

    def get_total_wage(self):
        total_wage = 0
        for item in self.__list_employees:
            total_wage += item.get_wage()
        return total_wage


class Employees:
    def __init__(self, name='', salay=0):
        self.name = name
        self.salary = salay

    def get_wage(self):
        pass


class Programmer(Employees):
    def __init__(self, name='', salary=0, share_money=0):
        super().__init__(name, salary)
        self.share_money = share_money

    def get_wage(self):
        super().get_wage()
        return self.salary + self.share_money


class Tester(Employees):
    def __init__(self, name='', salary=0, bug_number=0):
        super().__init__(name, salary)
        self.bug_number = bug_number

    def get_wage(self):
        super().get_wage()
        return self.salary + self.bug_number * 5


em = EmployeesManager()
em.add_employees(Programmer('八戒', 8000, 2000))
em.add_employees(Programmer('悟空', 18000, 4000))
em.add_employees(Tester('唐僧', 7000, 30))
em.add_employees(Tester('张三', 5000, 60))
print(em.get_total_wage())

for item in em.get_list_employees():
    print(item.name, item.get_wage())
