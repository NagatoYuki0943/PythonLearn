'''
命名元组,像对象一样

'''

from collections import namedtuple

# 三种定义命名元组的方法：第一个参数是命名元组的构造器（如下的：Person，Human） 效果完全一样
Person = namedtuple('Person', ['age', 'height', 'name'])
Human  = namedtuple('Human', 'age, height, name')
Human2 = namedtuple('Human2', 'age height name')

# 实例化命令元组
tom = Person(30, 188, 'Tom')
print(tom)
# Person(age=30, height=188, name='Tom')


jack = Human(20,179,'Jack')
print(jack)
# Human(age=20, height=179, name='Jack')


# 获取数据
print(tom.age)      # 30
print(jack.height)  # 179