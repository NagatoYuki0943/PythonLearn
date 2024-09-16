"""
调用时机:
        1. print(对象), 会自动调用 __str__ 方法, 打印输出的结果是 __str__ 方法的返回值
        2. str(对象)  类型转换,将自定义对象转换为字符串的时候, 会自动调用
应用:
        1. 打印对象的时候,输出一些属性信息
        2. 需要将对象转换为字符串类型的时候
注意点:
        方法必须返回一个字符串,只有 self 一个参数,不然就报错

没有定义 __str__ 默认print(对象)和str(对象)会输出对象的引用地址
"""


class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # print(对象) 和 str(对象) 会调用,对象转换为字符串
    # 参数只能由 self, 必须返回字符串
    def __str__(self):
        return f"敢打印我就鲨了你,name is {self.name},age is {self.age}"


# 没有定义 __str__ 默认print(对象)输出对象的引用地址


dog = Dog("大黄", 2)
print(dog)  # 敢打印我就鲨了你,name is 大黄,age is 2
res = str(dog)
print(res)  # 敢打印我就鲨了你,name is 大黄,age is 2
