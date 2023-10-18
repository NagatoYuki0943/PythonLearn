"""
setattr() 函数对应函数 getattr()，用于设置属性值，该属性不一定是存在的
语法
    setattr(object, name, value)
参数
    object -- 对象
    name -- 字符串，对象属性
    value -- 属性值

setattr可以在类中使用，参数1为self，设置对象参数
"""


class Letter():
    def __init__(self):
        self.a = 1


letter = Letter()
print(hasattr(letter, 'a'))     # True
print(hasattr(letter, 'b'))     # False

setattr(letter, 'b', 2)
print(hasattr(letter, 'a'))     # True
print(hasattr(letter, 'b'))     # True
print('\n')


#------------------------------------------#
#   setattr可以在类中使用，参数1为self，设置对象参数
#------------------------------------------#
class Coordinate():
    def __init__(self):
        self.x = 1

    def set(self):
        setattr(self, 'y', 2)

point1 = Coordinate()
print(hasattr(point1, 'x'))     # True
print(hasattr(point1, 'y'))     # False

point1.set()
print(hasattr(point1, 'x'))     # True
print(hasattr(point1, 'y'))     # True