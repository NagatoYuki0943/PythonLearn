'''
python中子类会继承父类的构造函数,字符串输出函数等,php也会继承构造函数
重写之后子类要调用父类的构造方法,给对象添加从父类继承的属性,
子类init方法中的形参,一般都写父类的形参,在写父类的形参

def __init__(self, name, color):
    # 子类要调用父类构造函数
    #Dog.__init__(self, name)
    #super(XTQ, self).__init__(name)
    super().__init__(name)
    self.color = color

/**
 * C++子类继承不能继承父类的构造函数,
 * C#子类继承不能继承父类的构造函数
 * PHP子类可以继承父类的构造和析构方法(php中构造方法是普通方法,遵循普通方法规律)
 *      要注意继承时父类的构造方法的初始化也对子类有效
 */
class Vehicle {
public:
    //父类构造方法有参数
    Vehicle(string name) {
        m_Name = name;
    }

    string m_Name;
};

class Car : public Vehicle {
public:

    /**
     * 子类要这样写才不会出错,要把子类的参数传给父类
     */
    Car(string name) : Vehicle(name) {
        m_Name = name;
    }
};
'''


class Dog(object):
    def __init__(self, name):
        self.name = name
        self.age = 0

    def __str__(self):
        return f"名字为:{self.name},年龄为:{self.age}"


class XTQ(Dog):
    def __init__(self, name, color):
        # 子类要调用父类构造函数
        #Dog.__init__(self, name)
        #super(XTQ, self).__init__(name)
        super().__init__(name)
        self.color = color

    def __str__(self):
        return f"名字为:{self.name},年龄为:{self.age},毛色为:{self.color}"


# 没有重写父类的构造函数和字符串输出函数
# xtq = XTQ('小黄')
# print(xtq)  # 名字为:小黄,年龄为:0


# 重写父类的构造函数
xtq = XTQ('小黄', '白色')
print(xtq)
# 名字为:小黄,年龄为:0,毛色为:白色