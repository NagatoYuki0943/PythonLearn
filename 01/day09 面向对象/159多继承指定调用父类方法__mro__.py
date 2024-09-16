"""
类名.__mro__ 查看当前类的继承顺序链,也叫作方法的调用顺序
    顺序 子类,继承类1,继承类2...object

重写方法,在重写的方法中调用父类方法
方法1 父类.方法(self, 其他参数)  建议这个

方法2 super(类A,self).方法(参数)  调用类A的父类(继承顺序链的下一个类)中的方法

super().方法(参数)  这个方法没有指定父类,因此会默认调用第一个继承类

/**
 * C++允许一个类继承多个类
 * 语法 class 子类 : 继承方式 父类1 , 继承方式,父类2...
 * 多继承可能会引发父类中有同名成员出现,需要加作用域加以区分   s1.Base1::m_A     s1.Base2::m_A
 * C++实际开发中不建议使用多继承
 */
"""


class God(object):
    def play(self):
        print("在云中飘...")

    def eat(self):
        print("吃仙桃")


class Dog(object):
    def bark(self):
        print("汪汪叫")

    def eat(self):
        print("吃骨头")


# 多继承
class XTQ(God, Dog):
    def eat(self):
        print("吃狗肉")

        # 方法1  父类.方法(self, 其他参数)
        God.eat(self)

        # 方法2 super(类A,self).方法(参数)  调用类A的父类(继承顺序链的下一个类)中的方法
        super(XTQ, self).eat()
        super(God, self).eat()
        super().eat()


xtq = XTQ()
xtq.eat()  # 吃狗肉
# 吃狗肉       print('吃狗肉')
# 吃仙桃       God.eat(self)
# 吃仙桃       super(XTQ, self).eat()  调用 XTQ 下一个类的方法
# 吃骨头       super(God, self).eat()  调用 GOd 下一个类的方法
# 吃仙桃       super().eat()           调用第一个类的方法


# 类名.__mro__ 查看当前类的继承顺序链,也叫作方法的调用顺序
print(
    XTQ.__mro__
)  # (<class '__main__.XTQ'>, <class '__main__.God'>, <class '__main__.Dog'>, <class 'object'>)
