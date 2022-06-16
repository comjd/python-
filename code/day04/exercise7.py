"""
    在控制台中录入学生信息（姓名、性别、年龄、成绩），姓名为空时推出录入
    输出所有学生的基本信息
"""
student_list = []
while True:
    name = input('请输入学生的姓名：')
    if name == "":
        break
    sex = input('请输入学生的性别：')
    age = input('请输入学生的年龄：')
    score = input('请输入学生的成绩：')
    student_info_dict = {'name': name, 'sex': sex, 'age': age, 'score': score}
    student_list.append(student_info_dict)
print(student_list)
for i in student_list:
    print(i['name'], i['sex'], i['age'], i['score'])
