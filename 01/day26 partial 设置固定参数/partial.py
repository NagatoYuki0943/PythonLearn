'''
partial可以给函数或类添加默认参数
新函数/类 = partial(函数/类, 默认参数)
'''

from functools import partial


def func1(a, b, c):
    return a + b * c

# partial 接收函数 multiply 作为参数，固定 multiply 的参数 y=2
func1 = partial(func1, b=2, c=3)

print(func1(1)) # 7
print(func1(2)) # 8

# b定义了固定值,给c传入参数的时候必须使用字典传值
func1 = partial(func1, b=2)
print(func1(1, c=3))        # 7

# 可以覆盖partial的值
print(func1(1, b=2, c=3))   # 7


class Obj(object):
    def __init__(self, name) -> None:
        self.name = name
Obj = partial(Obj, name="Tom")

obj = Obj()
print(obj.name)  # Tom

obj = Obj(name='Jerry')
print(obj.name)  # Jerry