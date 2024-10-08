"""
实例方法: 类中定义的方法就是实例方法
    第一个参数为self,表示实例对象

类方法: 使用 @classmethod 装饰的方法称为类方法
    第一个参数是 cls, 代表类对象自己,调用时不需要手动传递,python解释器会自动传递

    通过 对象.类方法() 调用
    通过 类名.类方法() 调用

1.在方法中使用了实例属性,该方法必须是实例方法
2.不需要使用实例属性,需要使用类属性,可以定义为类方法
3.不需要使用实例属性,也不需要使用类属性,可以定义静态方法
"""


class Dog(object):
    # 类方属性(类似静态属性)
    class_name = "狗类"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def play(self):
        print(f"小狗{self.name}在快乐的玩耍")

    # 实例方法,没有用到实例属性,所以可以定义为类方法
    def get_class0(self):
        return self.class_name

    # 类方法
    @classmethod
    def get_class1(
        cls,
    ):  # cls 代表类对象自己,调用时不需要手动传递,python解释器会自动传递
        return cls.class_name


dog = Dog("大黄", 15)
print(dog.get_class0())  # 狗类

# 可以通过 对象.类方法() 调用
print(dog.get_class1())  # 狗类

# 通过 类名.类方法() 调用
print(Dog.get_class1())  # 狗类
