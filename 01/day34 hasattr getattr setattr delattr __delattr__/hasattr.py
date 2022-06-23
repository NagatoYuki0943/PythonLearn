#-------------------------------------------------------------#
#   hasattr() 函数用于判断对象是否包含对应的属性
#   语法：
#       hasattr(object, name)
#   参数：
#       object -- 对象
#       name   -- 字符串，属性名
#   返回值：
#       如果对象有该属性返回 True，否则返回 False
#
#   hasattr可以在类内部使用，参数1为self，可以查看对象自身的属性
#-------------------------------------------------------------#


class Coordinate():
    x = 10
    y = -5
    def __init__(self):
        self.z = 0

point1 = Coordinate()
print(hasattr(point1, 'x'))     # True
print(hasattr(point1, 'y'))     # True
print(hasattr(point1, 'z'))     # True
print(hasattr(point1, 'no'))    # False


# hasattr可以在类内部使用，参数1为self，可以查看对象自身的属性
class RepVGGBlock():
    def __init__(self, deploy=False):
        if deploy:
            self.rbr_reparam = 1

    def forward(self):
        if hasattr(self, 'rbr_reparam'):
            print(1)
        else:
            print(0)

block1 = RepVGGBlock()
block1.forward()         # 0

block2 = RepVGGBlock(deploy=True)
block2.forward()         # 1