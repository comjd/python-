"""
    汇率换算
"""
# １、获取输入的值　美元
usp = input('请输入美元：')
# ２、逻辑计算　
rmb = float(usp) * 7.1477
# ３、输出结果　人民币
print('%.2f美元等于%.2f人民币'%(float(usp) ,rmb))
