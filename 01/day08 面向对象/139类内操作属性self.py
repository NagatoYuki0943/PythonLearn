"""
python self 在类内操作属性
    self 作为类中方法的第一个形参,在通过对象调用方法的时候,不需要手动的传递实参值,
    是python解释器自动调用该方法的对象传递给self,所以self指的是对象本身

    self是形参名字,可以改成别的名字,一般不改


C++ 和 php 中使用的是 this 操作内部属性,C++中可以省略它
    php中 self 和 static 调用静态属性和方法,他俩差异在下面

    php中 self和static区别
        在函数引用上，self与static的区别是：对于静态成员函数，self指向代码当前类，static指向调用类；
        对于非静态成员函数，self抑制多态，指向当前类的成员函数，static等同于this，动态指向调用类的函数。
        parent、self、static三个关键字联合在一起看挺有意思，分别指向父类、当前类、子类，有点“过去、现在、未来”的味道。

"""


class Dog(object):
    def play(self):
        print(f"self:{id(self)}")

    def show_name(self):
        print(f"name is {self.name}")


dog = Dog()
print(id(dog))  #      1506201209536
dog.play()  # self:1506201209536    self指的是对象本身,其他语言一般使用this
dog.name = "小明"
dog.show_name()  # name is 小明
