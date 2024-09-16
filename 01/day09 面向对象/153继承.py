"""
子类能用父类的属性和方法

继承语法
class 子类(父类):

self在子类调用子类属性和方法,在父类调用父类和方法,
php 在函数引用上，self与static的区别是：对于静态成员函数，self指向代码当前类，static指向调用类；
    对于非静态成员函数，self抑制多态，指向当前类的成员函数，static等同于this，动态指向调用类的函数。
"""


class Animal(object):
    def __init__(self):
        self.name = "Animal"

    def speak(self):
        print(self.name)


class Dog(Animal):
    def __init__(self):
        super().__init__()
        self.name = "dog"


# self在子类调用子类属性和方法,在父类调用父类和方法,php中self调用父类静态属性和方法,而static调用静态属性和方法
animal = Animal()
animal.speak()  # Animal
dog = Dog()
dog.speak()  # Dog
