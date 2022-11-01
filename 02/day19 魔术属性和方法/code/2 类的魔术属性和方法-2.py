'''
魔法属性:
    __dict__ 获取对象或者类的信息
        获取对象信息 `对象名.__dict__`  对象的实例属性信息
        获取类的信息 `类名.__dict__`   模块、类描述、对象方法...


魔法方法:
    __call__  对象当做函数使用时会调用它

    __str__   打印对象时输出的数据
        str方法一定要return，而且return 一定字符串内容

    用字典的书写格式操作对象的方法
        `__getitem__ `   对象['属性名']
        `__setitem__ `   对象['属性名'] = 值
        `__delitem__ `   del 对象['属性名']


'''
from typing import Any



class Goods(object):
    """这是一个商品类"""

    goods_color = "transparent"

    def __init__(self) -> None:
        self.name ="牛仔裤"


    def set_price(self, val):
        """
        这是价格的方法
        val: number 设置的价格
        """
        pass

        # 对象当做函数使用时会调用它
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print("__call__")


    # __str__   打印对象时输出的数据, 一定要返回数据
    def __str__(self) -> str:
        return "我是goods对象"


    # 用字典的书写格式操作对象的方法
    def __getitem__(self, item):
        print('item: ', item)


    # 用字典的书写格式操作对象的方法
    def __setitem__(self, key, value):
        print('key: ', key, ',value: ', value)


    # 用字典的书写格式操作对象的方法
    def __delitem__(self, key):
        print('key: ', key)


# __call__ 对象当做函数使用时会调用它
Goods()()           # __call__

goods = Goods()
goods()             # __call__


# __str__ 打印对象时输出的数据
print(Goods)        # <class '__main__.Goods'>

print(goods)        # 打印类默认打印: <__main__.Goods object at 0x000002C24CE4A400>
                    # 我是goods对象


# __dict__ 打印类或对象的属性,返回字典
print(Goods.__dict__)
# {'__module__': '__main__', '__doc__': '这是一个商品类', 'goods_color': 'transparent', 'set_price': <function Goods.set_price at 0x000001CEF0750510>, '__call__': <function Goods.__call__ at 0x000001CEF0750598>, '__str__': <function Goods.__str__ at 0x000001CEF0750620>, '__dict__': <attribute '__dict__' of 'Goods' objects>, '__weakref__': <attribute '__weakref__' of 'Goods' objects>}

print(goods.__dict__)
# {'name': '牛仔裤'}

print('-' * 50)


# 用字典的书写格式操作对象的方法,访问  __getitem__  __setitem__  __delitem__
goods['a']          # item:  a

goods['b'] = 10     # key:  b ,value:  10

del goods['c']      # key:  c

