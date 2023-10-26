'''
直接打印列表,输出的是里面的值,而将自己的对象放进列表,打印的却是地址
原因是自己的类中没有定义 __repr__ 方法

repr方法和str方法非常类似,也是必须返回一个字符串,然后在打印容器时就能正确输出值了

如果没有定义 __str__ 只定义了 __repr__, 在触发 __str__ 的时候就会调用 __repr__

'''

# 列表中存储了3个字符串对象
list1 = ['hello', 'python', 'cpp']
print(list1)    # ['hello', 'python', 'cpp']    直接输出值,而不是地址


class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name},{self.age}岁"

    # repr方法和str方法非常类似,也是必须返回一个字符串,然后在打印容器时就能正确输出值了
    def __repr__(self):
        return f"{self.name}"


list2 = [Dog('a', 1), Dog('b', 2)]
print(list2)    # [<__main__.Dog object at 0x000001F0A3B20FD0>, <__main__.Dog object at 0x000001F0A3B20F10>]