'''
`collections.defaultdict(default_factory)`为字典的没有的key提供一个默认的值。
参数应该是一个函数，当没有参数调用时返回默认值。如果没有传递任何内容，则默认为None。

就是取字典的key不存在时不会报错
defaultdict(存放的数据类型)
'''

from collections import defaultdict


d = defaultdict()
print(d)
# defaultdict(None, {})
e = defaultdict(str)
print(e)
# defaultdict(<class 'str'>, {})
print('-' * 50)


d = defaultdict(str)
print(d)
# defaultdict(<class 'str'>, {})

d['hello']
print(d)
# defaultdict(<class 'str'>, {'hello': ''})


# 普通字典调用不存在的键时，将会抛异常
e = {}
print(e['hello'])
# Traceback (most recent call last):
#   File "d:/Python/Pycharm/01/day11补/collections defaultdict.py", line 20, in <module>
#     print(e['hello'])
# KeyError: 'hello'
print('-' * 50)


# dict存放的数据类型是int
fruit = defaultdict(int)
fruit['apple'] += 2 
print(fruit)    # defaultdict(<class 'int'>, {'apple': 2})
fruit['apple'] += 2 
print(fruit)    # defaultdict(<class 'int'>, {'apple': 4})

# 没有对象时，返回0
print(fruit['banana'])
print(fruit)    # defaultdict(<class 'int'>, {'apple': 4, 'banana': 0})
print('-' * 50)


s = [('NC', 'Raleigh'), ('VA', 'Richmond'), ('WA', 'Seattle'), ('NC', 'Asheville')]

# dict存放的数据类型是list
d = defaultdict(list)
for k, v in s:
    d[k].append(v)
print(d)
# defaultdict(<class 'list'>, {'NC': ['Raleigh', 'Asheville'], 'VA': ['Richmond'], 'WA': ['Seattle']})
