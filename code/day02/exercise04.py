"""
    请输入季度
"""
while True:
    season = input("请输入季度（春、夏、秋、冬中的一个）：")
    if season == '春':
        print('1月２月３月')
    elif season == '夏':
        print('4月5月6月')
    elif season == '秋':
        print('7月8月9月')
    elif season == '冬':
        print('10月11月12月')
    else:
        print('季节输入错误')
    if season == 'exit':
        break
