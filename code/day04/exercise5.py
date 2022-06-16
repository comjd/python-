"""
    在控制台输入商品的名称和价格
    当商品名称为空的时候推出录入
    输出录入的所有商品名称及价格
"""
list_of_goods = {}
while True:
    name = input('请输入商品名称：')
    if name == "":
        break
    price = input('请输入商品价格：')
    list_of_goods[name] = price
for k, v in list_of_goods.items():
    print(k, v)
