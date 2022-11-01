'''
四个方法名相同

@ property         获取属性
@ 方法名.getter     获取属性,和@property相同,不用写
    @ property
    def 方法名(self):
        pass

@ 方法名.setter     设置属性
    @ price.setter
    def price(self, val):

@ 方法名.deleter    删除属性
    @ price.deleter
    def price(self):

类: Goods
方法:
    1.初始化方法
    2.获取价格
    3.设置价格
    4.删除价格
'''

class Goods(object):
    def __init__(self) -> None:
        self.org_price = 1000
        self.discount = 0.7


    # 2.获取价格
    @ property
    def price(self):
        return self.org_price * self.discount


    # @ property 实现了 getter方法,所以不用写
    @ price.getter
    def price(self):
        return self.org_price * self.discount


    # 3.设置价格
    @ price.setter
    def price(self, val):
        if val > 0:
            self.org_price = val


    # 4.删除价格
    @ price.deleter
    def price(self):
        print("执行了deleter方法")
        self.org_price = 0.00


goods = Goods()

# 获取
print(goods.price)      # 700.0

# 设置
goods.price = 700
print(goods.price)      # 489.99999999999994

# 设置错误值
goods.price = -700
print(goods.price)      # 489.99999999999994

# 删除值
del goods.price
print(goods.price)
# 执行了deleter方法
# 0.0
