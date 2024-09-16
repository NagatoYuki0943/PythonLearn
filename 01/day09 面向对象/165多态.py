"""
传入父类对象,但是也能传入子类对象,得到不同的结果
1.子类继承父类
2.子类重写父类方法
3.通过对象调用这个方法

python中多态可以没有继承,叫鸭子类型,
"""


class Dog(object):
    def __init__(self, name):
        self.name = name

    def play(self):
        print(f"{self.name}正在玩耍")


class XTQ(Dog):
    # 重写父类方法
    def play(self):
        print(f"{self.name}在天上追云彩")


class Cat(object):
    def __init__(self, name):
        self.name = name

    def play(self):
        print(f"{self.name}在玩毛线")


# 参数是父类,可以传入父类或子类,分别调用不同方法
def play_with_dog(obj_dog):
    obj_dog.play()


dog = Dog("小明")
play_with_dog(dog)  # 小明正在玩耍


xtq = XTQ("哮天犬")
play_with_dog(xtq)  # 哮天犬在天上追云彩


# cat不继承Dog类,但是也能调用
cat = Cat("喵喵喵")
play_with_dog(cat)  # 喵喵喵在玩毛线
