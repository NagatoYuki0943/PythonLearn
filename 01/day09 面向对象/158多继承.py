'''
class 子类(父类1, 父类2)
class XTQ(God, Dog)

两个父类出现同名方法,子类对象调用的是第一个继承父类中的方法

/**
 * C++允许一个类继承多个类
 * 语法 class 子类 : 继承方式 父类1 , 继承方式,父类2...
 * 多继承可能会引发父类中有同名成员出现,需要加作用域加以区分   s1.Base1::m_A     s1.Base2::m_A
 * C++实际开发中不建议使用多继承
 */
'''


class God(object):

    def play(self):
        print('在云中飘...')

    def eat(self):
        print('吃仙桃')


class Dog(object):

    def bark(self):
        print('汪汪叫')

    def eat(self):
        print('吃骨头')


# 多继承
class XTQ(God, Dog):
    pass


xtq = XTQ()
# 这个方法只有God类中有
xtq.play()  # 在云中飘...

# 这个方法只有Dog类中有
xtq.bark()  # 汪汪叫

# 这个方法两个父类都有 调用的是前边继承的类内的方法
xtq.eat()   # 吃仙桃