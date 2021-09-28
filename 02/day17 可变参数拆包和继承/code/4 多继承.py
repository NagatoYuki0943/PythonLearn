'''
初始化顺序是mro的反方向调用
'''

# 定义父类Parent
class Parent(object):
    def __init__(self, name, *args, **kwargs):

        self.name = name
        print('parent的init结束被调用')


# 定义子类  Son1 --继承--> Parent
class Son1(Parent):
    def __init__(self, name, age, *args, **kwargs):

        self.age = age
        super().__init__( name, *args, **kwargs)
        print('Son1的init结束被调用')


# 定义子类  Son2 --继承--> Parent
class Son2(Parent):
    def __init__(self, name, gender, *args, **kwargs):

        self.gender = gender
        super().__init__(name, *args, **kwargs)
        print('Son2的init结束被调用')


# 定义子类  Grandson --继承--> Son1 / Son2
class Grandson(Son1, Son2):
    def __init__(self, name, age, gender):

        super().__init__(name, age, gender)  # 单独调用父类的初始化方法
        # Son2.__init__(self, name, gender)
        print('Grandson的init结束被调用')


# 创建对象
gs = Grandson('grandson', 12, '男')
print(Grandson.mro())
# 初始化顺序是mro的反方向调用
# parent的init结束被调用
# Son2的init结束被调用
# Son1的init结束被调用
# Grandson的init结束被调用
# [<class '__main__.Grandson'>, <class '__main__.Son1'>, <class '__main__.Son2'>, <class '__main__.Parent'>, <class 'object'>]


