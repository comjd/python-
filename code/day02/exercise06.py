"""
    请输入成绩
"""
score = float(input('请输入成绩：'))
if score < 0 or score > 100:
    print('你输入的成绩有误')
elif score >= 90:
    print('优秀')
elif score >= 80:
    print('良好')
elif score >= 60:
    print('及格')
else:
    print('不及格')
