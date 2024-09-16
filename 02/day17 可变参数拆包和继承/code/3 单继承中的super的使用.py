class Parent(object):
    def __init__(self, name):
        self.name = name
        print("parent的init结束被调用")


class Son(Parent):
    def __init__(self, name, age):
        self.age = age
        super().__init__(name)
        print("Son1的init结束被调用")


class Grandson(Son):
    def __init__(self, name, age, gender):
        self.gender = "男"
        super().__init__(name, age)  # 单继承不能提供全部参数
        print("Grandson的init结束被调用")


gs = Grandson("grandson", 12, "男")

# 继承链
print(Grandson.__mro__)
print("姓名：", gs.name)
print("年龄：", gs.age)
print("性别：", gs.gender)

# (<class '__main__.Grandson'>, <class '__main__.Son'>, <class '__main__.Parent'>, <class 'object'>)
# 姓名： grandson
# 年龄： 12
# 性别： 男
