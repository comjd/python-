"""
    公司有以下员工：
    经理：曹操,刘备,孙权
    技术：操,刘备,张飞,关羽
    请计算：
        是经理也是技术的有谁？
        是经理，不是技术的有谁？
        是技术，不是经理的有谁？
        身兼一职的有谁？
        经理和技术总共多少人？
"""
manager_set = {'曹操', '刘备', '孙权'}
tech_set = {'曹操', '刘备', '张飞', '关羽'}
# 集合交集
print('是经理也是技术的有谁:', manager_set & tech_set)
#　集合差集
print('是经理，不是技术的有谁:', manager_set - tech_set)
print('是技术，不是经理的有谁:', tech_set - manager_set)
# 集合补集
print('身兼一职的有谁:', tech_set ^ manager_set)
# 集合并集
print('经理和技术总共多少人:', len(tech_set | manager_set))
