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
