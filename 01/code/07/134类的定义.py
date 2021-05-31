'''
类名遵循大驼峰

新式类: 直接或者间接继承 object
旧式类:
在py3中所有类默认继承object类,即py3中没有旧式类
'''


# 语法1  object是所有类的基类
class Dog(object):
    pass


# 语法2
class Cat():
    pass


# 语法3
class Mouse:
    pass