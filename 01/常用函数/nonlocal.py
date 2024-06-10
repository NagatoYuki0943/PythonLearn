"""nonlocal 关键字"""


def f():
    x = 1
    print(x)

    def g():
        # 当一个闭包尝试修改它的外部变量时，需要使用 nonlocal 关键字
        nonlocal x
        x = 2

    g()
    print(x)


f()
# 1
# 2


def f():
    x = 3
    print(x)

    class C:
        def g(self):
            # 当一个闭包尝试修改它的外部变量时，需要使用 nonlocal 关键字
            nonlocal x
            x = 4

    c = C()
    c.g()
    print(x)

f()
# 3
# 4


# 不过要主要下面全局变量是可变类型,在函数中修改全局变量是可以的,但是不能使用 = 赋值,否则就变为局部变量

def f():
    d = []

    def g():
        d.append(1)

    g()
    print(d)    # [1]


f()
