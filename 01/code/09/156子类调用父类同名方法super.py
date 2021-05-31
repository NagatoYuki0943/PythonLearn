'''
通过对象调用方法,不需要传递实参值,python解释器会自动将对象作为实参值传递给self形参,
如果是通过类名.方法() 调用则python解释器就不会自动传递实参值,需要手动self

方法1: 父类名.方法名(self)  必须要有self
    Dog.bark(self, 其他参数)

方法2  父类名(参数).方法名() 不推荐使用
    Dog().bark()  这个函数没实参

方法3 super(类A, self).方法名(参数)   调用类A的父类(继承顺序链的下一个类)中的方法
    super(Xiao_tian_quan,self).bark()

方法4: super().方法名(参数)  方法3的简写
        super().bark()

/**
 * C++中子类调用父类同名方法
 *
 * 访问子类同名成员,直接访问即可
 * 访问父类同名成员,需要加作用域
 *      class Son
 *      class Son : public Base
 *      通过子类对象访问父类中同名成员属性  s1.Base::m_A
 *      通过子类对象调用父类同名函数       s2.Base::func();
 *      调用父类中的重载函数              s2.Base::func(10);
 *   如果子类中出现和父类同名的函数成员函数,子类的同名成员会隐藏掉父类中所有的同名函数(重载函数也会被影藏)
 *   要用Base::方式访问父类中的重载函数
 *
 * 静态成员和非静态成员出现同名,处理方式一样
 * 静态成员:静态数据:所有对象共享同一份数据;类内声明,类外初始化;编译阶段分配内存
 *        静态成员函数:所有对象共享同一份数据;访问静态成员变量
 *      访问子类同名成员,直接访问即可
 *      访问父类成员,需要加作用域
 *
 *  s.m_A        === Son::m_A        s.func()       == Son::func()         //子类
 *  s.Base::m_A  === Son::Base::m_A  s.Base::func() == Son::Base::func()   //父类
 *                   前一个::是通过类名Son方式访问,第二个::是访问Sase作用域下的m_A
 */

 /**
  * php使用 parent::父类方法() 调用父类方法,无论静态,动态都使用parent::
  *
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


    def see_host(self):
        # 调用子类自己的方法
        self.bark()


    # 子类调用父类方法
    def see_hosts(self):
        # 方法1: 父类名.方法名(self, 其他参数), self必须有
        Dog.bark(self)

        # 方法2:  父类名(参数).方法名() 不推荐使用
        #Dog().bark()

        # 方法3: super(当前类, self).方法名(参数)   调用当前类的父类中的方法
        super(Xiao_tian_quan,self).bark()

        # 方法4: super().方法名(参数)  方法3的简写
        super().bark()


xiao_tian_quan = Xiao_tian_quan()
xiao_tian_quan.see_host()   # 吼吼吼

# 子类调用父类方法
xiao_tian_quan.see_hosts()
# 汪汪汪
# 汪汪汪
# 汪汪汪