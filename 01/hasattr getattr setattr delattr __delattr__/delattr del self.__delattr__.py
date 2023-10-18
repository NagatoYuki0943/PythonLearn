"""
delattr 函数用于删除属性
delattr(x, 'foobar') 相等于 del x.foobar。
语法：
    delattr(object, name)
参数：
    object -- 对象
    name   -- 必须是对象的属性

在类中也能使用，参数1为self，也能使用 del函数 和 self.__delattr__
    delattr(self, 'name')
    del self.属性
    self.__delattr__('name')

删除不存在的值会报错
"""


class Coordinate:
    x = 10
    y = -5
    z = 0


point1 = Coordinate()

print(point1.x)     # 10
print(point1.y)     # -5
print(point1.z)     # 0

delattr(Coordinate, 'z')

print('--删除 z 属性后--')
print(point1.x)     # 10
print(point1.y)     # -5

try:
    # 触发错误
    print(point1.z)
except:
    print('删除z失败，没有z') # 删除z失败，没有z


class Letter():
    def __init__(self) -> None:
        self.a = 1
        self.b = 2
        self.c = 3
        self.d = 4

    def delete(self):
        # 三行效果相同
        delattr(self, 'a')
        del self.b
        self.__delattr__('c')

letter = Letter()
print(hasattr(letter, 'a'))     # True
print(hasattr(letter, 'b'))     # True
print(hasattr(letter, 'c'))     # True
print(hasattr(letter, 'd'))     # True

letter.delete()
print(hasattr(letter, 'a'))     # False
print(hasattr(letter, 'b'))     # False
print(hasattr(letter, 'c'))     # False
print(hasattr(letter, 'd'))     # True


# 删除不存在的值会报错
delattr(letter, 'x')            # AttributeError: x