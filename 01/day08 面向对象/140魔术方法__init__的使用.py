'''
在 python 的类中,有一类方法,这类方法以 `两个下划线开头` 和`两个下划线结尾`, 并且在`满足某个特定条件的情况下,会自动调用`. 这类方法,称为魔法方法

作用:
	1. 用来给对象添加属性,给对象属性一个初始值(构造函数)
	2. 代码的业务需求,每创建一个对象,都需要执行的代码可以写在 `__init__ `中
注意点: 如果 __init__ 方法中,有出了 self 之外的形参,那么在创建的对象的时候,需要给额外的形参传递实参值 `类名(实参)`

php中是 __construct__(){}

C++中构造函数是 类名(){}    根据参数不同可以设置多个构造函数 太牛逼了
    析构函数是 ~类名(){}  析构函数不能有参数
'''

class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f'My name is {self.name}, age is {self.age}')


# 传递实参值
dog = Dog('小明', 18)
dog.show_info()
