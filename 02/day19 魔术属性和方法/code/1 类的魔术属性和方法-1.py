'''
魔术属性

    __doc__    获取描述信息
        获取类的
            类.__doc__
        获取方法的描述
            类.方法名.__doc__
            对象.方法.__doc__

    __module__ 获取所属的模块  直接改文件 获取的__main__
        类.__module__
        对象.__module__

    __class__ 获取对象所属的类
        对象.__class__


魔术方法
    __init__ 初始化方法
        类() 自动调用
    __del__  删除对象的时候，会调用  del 对象

'''

class Goods(object):
    """这是一个商品类"""

    def set_price(self, val):
        """
        这是价格的方法
        val: number 设置的价格
        """


# 获取描述信息
print(Goods.__doc__)
# 这是一个商品类

goods = Goods()
print(goods.__doc__)
# 这是一个商品类

print(Goods.set_price.__doc__)
# 这是价格的方法
# val: number 设置的价格

print(goods.set_price.__doc__)
# 这是价格的方法
# val: number 设置的价格

print('-' * 50)


# 获取所属的模块
print(Goods.__module__)
print(goods.__module__)
# __main__
# __main__

print('-' * 50)


# 获取对象所属的类
print(goods.__class__)
# <class '__main__.Goods'>
