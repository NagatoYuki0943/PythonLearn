'''
单继承: 如果一个类只有一个父类,这种关系就称为单继承
多继承: 如果一个类有多个父类,就称作多继承
多层继承: a --> b --> c
'''


class Animal(object):
    def __init__(self):
        self.name ='Animal'

    def speak(self):
        print(self.name)


# 单继承
class Dog(Animal):
    def __init__(self):
        super().__init__()
        self.name = 'Dog'

    def bark(self):
        print("汪汪叫")


# 多次继承
class Xiao_tian_quan(Dog):
    def __init__(self):
        super().__init__()
        self.name = '哮天犬'


xiao_tian_quan = Xiao_tian_quan()
xiao_tian_quan.speak()              # 哮天犬
xiao_tian_quan.bark()               # 汪汪叫