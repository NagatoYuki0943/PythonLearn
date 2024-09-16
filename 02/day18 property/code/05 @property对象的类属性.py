"""
BAR = property(get_bar, set_bar, del_bar, "BAR是Foo一个属性")
# 前三个是方法名,最后是字符串
# 第1个 当通过对象访问 foo.BAR          时调用第2个方法
# 第2个 当通过对象访问 foo.BAR = ??     时调用第2个方法
# 第3个 当通过对象访问 del foo.BAR      时调用
# 第4个 当通过类名访问 Foo.BAR.__doc__  时调用
"""


class Goods(object):
    def __init__(self) -> None:
        self.org_price = 1000
        self.discount = 0.7

    # 2.获取价格
    def get_price(self):
        return self.org_price * self.discount

    # 3.设置价格
    def set_price(self, val):
        if val > 0:
            self.org_price = val

    # 4.删除价格
    def del_price(self):
        print("执行了deleter方法")
        self.org_price = 0.00

    # 通过BAR访问类中的方法
    #              获取        设置        删除        文档
    BAR = property(get_price, set_price, del_price, "BAR是property的一个对象")


goods = Goods()

# 全通过BAR获取设置等

# 获取
print(goods.BAR)  # 700.0

# 设置
goods.BAR = 700
print(goods.BAR)  # 489.99999999999994

# 删除
del goods.BAR
print(goods.BAR)
# 执行了deleter方法
# 0.0

# 帮助文档
# 通过类名访问
print(Goods.BAR.__doc__)  # BAR是property的一个对象
