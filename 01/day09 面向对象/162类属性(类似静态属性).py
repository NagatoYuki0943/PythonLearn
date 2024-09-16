"""
对象(实例对象): 通过class类实例化来的,这个对象称为实例对象
    实例对象定义的属性称为 实例属性,
        通过实例对象或者通过self 定义的属性都称为实例属性
    实例属性: 每个对象都存在一份,并且值可能是不一样的

类(类对象): 通过class定义的,又称为类对象;类对象是python解释器在创建类的时候自动创建的
作用
    1: 通过类对象定义实例对象,
    2: 类对象可以保存属性信息,这些属性称为类属性

    在类内部,方法外部定义的对象就成为类属性
    类属性在内存中只有一份

访问类属性
    类名.类属性

修改类属性
    类名.类属性 = 属性值

如果不存在和实例属性同名的类属性,则可以使用实例对象访问类属性的值(只能访问,不能修改);
如果存在重名,则使用实例属性访问的一定是实例属性,不是实例属性

类属性在类内的方法中可以使用 self 之类的访问

实例对象自己用: 实例属性
实例对象一起用: 类属性
"""


class Dog(object):
    # 类属性
    class_name = "狗类"

    def __init__(self, name, age, class_name):
        # 定义的都是实例属性
        self.name = name
        self.age = age
        self.class_name = class_name


dog = Dog("阿黄", 18, "miao")

# 打印dog对象的属性
print(dog.class_name)  # 狗类
print(dog.__dict__)  # {'name': '阿黄', 'age': 18}     没有类属性


# 查看类的属性
print(Dog.__dict__)  # ... 'class_name': '狗类', ...


# 访问类属性
print(Dog.class_name)  # 狗类
Dog.class_name = "Dog"
print(Dog.class_name)  # Dog


# 重新赋值之后有对象属性和类属性
dog.class_name = "Miao"
print(dog.class_name)  # Miao
print(dog.__dict__)  # {'name': '阿黄', 'age': 18, 'class_name': 'Miao'}
print(Dog.__dict__)  # # ... 'class_name': 'Dog', ...


# 如果不存在和实例属性同名的类属性,则可以使用实例对象访问类属性的值(只能访问,不能修改);
# 如果存在重名,则使用实例属性访问的一定是实例属性,不是实例属性


print(Dog.class_time)
