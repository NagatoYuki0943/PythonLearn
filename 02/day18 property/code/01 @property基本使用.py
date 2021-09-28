'''
@property 装饰的方法，只能有一个参数self

@ property
def property(self):
    return self.number

装饰完之后,可以像使用属性一样使用方法,不用加括号
print(foo.property) # 100
'''

class Foo(object):

    # 初始化方法
    def __init__(self, number) -> None:
        self.number = number
    
    # 获取对象
    @ property
    def property(self):
        return self.number


foo = Foo(100)

# 装饰完之后,可以像使用属性一样使用方法,不用加括号
print(foo.property) # 100
print("----------------------------------")
