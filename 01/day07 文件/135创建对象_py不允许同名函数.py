"""
创建对象 不用new
变量 = 类名()

调用类方法
对象.方法名()

通过对象调用方法,不需要传递实参值,python解释器会自动将对象作为实参值传递给self形参,
如果是通过类名.方法() 调用则python解释器就不会自动传递实参值,需要手动self


python不允许同名函数,参数不同也不行
"""


class Dog(object):
    def play(self):
        print("小狗快乐的拆家中")

    # python不允许同名函数,参数不同也不行
    # def play(self, name):
    #     pass

    def eat(self, food):
        print(f"吃{food}")


dog = Dog()
print(id(dog))  # 2547036228288
dog.play()  # 小狗快乐的拆家中
dog.eat("狗肉")  # 吃狗肉


dog1 = Dog()
print(id(dog1))  # 2547036228240
