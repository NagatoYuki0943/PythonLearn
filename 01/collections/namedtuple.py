"""
命名元组,像对象一样
"""

from collections import namedtuple


# 三种定义命名元组的方法：第一个参数是命名元组的构造器（如下的：Person，Human） 效果完全一样
Person = namedtuple("Person", ["age", "height", "name"])
Human = namedtuple("Human", "age, height, name")
Pet = namedtuple("Pet", "category age name")


# 实例化命令元组
tom = Person(10, 188, "Tom")
print(tom)  # Person(age=10, height=188, name='Tom')
print(tom.age)  # 10


jerry = Human(8, 179, "Jerry")
print(jerry)  # Human(age=8, height=179, name='Jerry')
print(jerry.height)  # 179


duck = Pet("duck", 2, "Duck")
print(duck)  # Pet(category='duck', age=2, name='Duck')
print(duck.age)  # 2
