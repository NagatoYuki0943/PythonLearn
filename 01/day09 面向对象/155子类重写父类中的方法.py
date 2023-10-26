'''
重写: 子类定义和父类名字相同的方法.
为什么重写: 父类中的方法,不能满足子类对象的需求,所以要重写.
重写之后的特点: 子类对象调用子类自己的方法,不再调用的方法,父类对象调用父类自己的方法.

/**
 * php注意事项
 *
 * 注意
 * (1)  PHP没有同名函数,所以子类出现同名函数就是重写,C++和C#出现同名函数算是隐藏,使用了virtual或abstract才是重写
 *      PHP子类方法重写父类方法不能比父类更严格,即父类方法如果是public,子类方法必须是public;父类方法如果是protected,子类方法可以使public或protected
 *      C++中没有这条规则
 *      C#使用virtual/abstract和override重写时不能修改访问修饰符
 *
 * (2)  PHP7要求被重写的方法必须与父类保持参数一致(数量和类型)
 *      C++中没有这条规则
 *      C#使用virtual/abstract和override重写时也要参数一致(数量和类型),不是重写就没问题
 *      C#使用覆盖不是重写,(父类无参数,子类有参数)不给参数调用父类方法,给参数调用子类方法
 */

'''


class Dog(object):
    def __init__(self):
        self.name = 'Dog'

    def bark(self):
        print("汪汪汪")


class Xiao_tian_quan(Dog):
    def __init__(self):
        super().__init__()
        self.name = "哮天犬"

    def bark(self):
        print("吼吼吼")


# 重写后父类调用自己的方法,子类调用子类自己的方法
dog = Dog()
dog.bark()                          # 汪汪汪

xiao_tian_quan = Xiao_tian_quan()
xiao_tian_quan.bark()               # 吼吼吼