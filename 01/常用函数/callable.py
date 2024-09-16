"""
callable() 函数用于检查一个对象是否是可调用的。如果返回 True，object 仍然可能调用失败；但如果返回 False，调用对象 object 绝对不会成功。

对于函数、方法、lambda 函式、 类以及实现了 __call__ 方法的类实例, 它都返回 True。
"""

print(callable(0))  # False
print(callable("Hello"))  # False
print(callable(print))  # True


def foo(): ...


print(callable(foo))  # True


class NotEexc:
    def __init__(self) -> None: ...


print(callable(NotEexc()))  # False


class Exec:
    def __call__(self): ...


print(callable(Exec()))  # True
