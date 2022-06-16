"""
商品购买
"""
# 订单列表
order_info_list = []


def get_dict_commodity():
    """
    获取商品所以列表数据
    :return: 商品相信信息,类型[{},{}]
    """
    goods_list = [
        {'编号': 101, '名称': '屠龙刀', '价格': 9000},
        {'编号': 102, '名称': '倚天剑', '价格': 1000},
        {'编号': 103, '名称': '九阴真经', '价格': 9500},
        {'编号': 104, '名称': '降龙十八掌', '价格': 30000},
        {'编号': 105, '名称': '乾坤大挪移', '价格': 6000},
        {'编号': 106, '名称': '吸星大法', '价格': 13000},
    ]
    return goods_list


def print_commodity_info(goods_list):
    """
    打印商品信息
    :param goods_list:商品列表
    :return:
    """
    if goods_list is not None:
        for item in goods_list:
            print('编号：%s,名称：%s,价格:%d' % (item['编号'], item['名称'], item['价格']))


def get_goods_list_price(goods_list):
    """
    计算所有商品总价
    :param goods_list: 订单列表，[{}]
    :return:返回商品总价,int
    """
    total_price = 0
    if goods_list is not None:
        for item in goods_list:
            good = get_good_of_no(item['编号'])
            print('你购买了%s,购买数量%.2f,单价%.2f' % (good['名称'], float(item['数量']), float(good['价格'])))
            total_price += float(good['价格']) * float(item['数量'])
    return total_price


def get_good_of_no(no=101):
    """
    根据编号获取商品
    :param no: 传入商品编号
    :return: 返回商品信息
    """
    for item in get_dict_commodity():
        for k, v in item.items():
            if str(v) == str(no):
                return item


def buying():
    """
    购买商品
    :return:
    """
    print_commodity_info(get_dict_commodity())
    good_no = input('请输入购买的商品编号：')
    good_count = float(input('请输入购买数量：'))
    for i in order_info_list:
        if good_no == str(i['编号']):
            i['数量'] = float(i['数量']) + good_count
            break
    else:
        print(good_no, good_count)
        order_info_list.append({'编号': good_no, '数量': good_count})


def settlement():
    """
    订单结算
    :return:
    """
    global order_info_list
    total_amount = get_goods_list_price(order_info_list)
    print('你购买的商品总价是：%.2f' % total_amount)
    money = float(input('请输入支付金额：'))
    if money < total_amount:
        print('购买失败！')
        return False
    else:
        print('购买成功，找回金额为%.2f' % (money - total_amount))
        order_info_list = []
        return True


while True:
    input_str = input('1购买商品，2结算：')
    if input_str == '１' or input_str == '1':
        buying()
    else:
        if settlement():
            break
