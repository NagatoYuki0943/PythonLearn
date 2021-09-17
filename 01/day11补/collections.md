# Python中collections模块

这个模块实现了特定目标的容器，以提供Python标准内建容器 dict、list、set、tuple 的替代选择。

- Python中collections模块
    - Counter：字典的子类，提供了可哈希对象的计数功能
    - defaultdict：字典的子类，提供了一个工厂函数，为字典查询提供了默认值
    - OrderedDict：字典的子类，保留了他们被添加的顺序
    - namedtuple：创建命名元组子类的工厂函数
    - deque：类似列表容器，实现了在两端快速添加(append)和弹出(pop)
    - ChainMap：类似字典的容器类，将多个映射集合到一个视图里面

## Counter 计数

**Counter是一个dict子类，主要是用来对你访问的对象的频率进行计数。**
 常用方法：

- elements()：返回一个迭代器，每个元素重复计算的个数，如果一个元素的计数小于1,就会被忽略。
- most_common([n])：返回一个列表，提供n个访问频率最高的元素和计数
- subtract([iterable-or-mapping])：从迭代对象中减去元素，输入输出可以是0或者负数
- update([iterable-or-mapping])：从迭代对象计数元素或者从另一个 映射对象 (或计数器) 添加。

```python
from collections import Counter


ls = [2, 3, 4, 2, 4, 4, 5, 3, 1, 4, 9, 0, 1, 0, 15, 0]
lr = [2, 3, 1, 0, 4, 0]


res = Counter(ls)
print(res)
# Counter({4: 4, 0: 3, 2: 2, 3: 2, 1: 2, 5: 1, 9: 1, 15: 1})
```

常用的方法：

```python
# 获取4的次数
print(res[4])   # 4

# 全部元素
print(res.elements())
# <itertools.chain object at 0x00000206AA4DAC50>
print(list(res.elements()))
# [2, 2, 3, 3, 4, 4, 4, 4, 5, 1, 1, 9, 0, 0, 0, 15]


# Counter之间可以相加减,可以对次数相加减
ret = Counter(lr)
print(res + ret)
# Counter({4: 5, 0: 5, 2: 3, 3: 3, 1: 3, 5: 1, 9: 1, 15: 1})

print(res - ret)
# Counter({4: 3, 2: 1, 3: 1, 5: 1, 1: 1, 9: 1, 0: 1, 15: 1})
```

## defaultdict 默认值

`collections.defaultdict(default_factory)`为字典的没有的key提供一个默认的值。参数应该是一个函数，当没有参数调用时返回默认值。如果没有传递任何内容，则默认为None。

**就是取字典的key不存在时不会报错**

**defaultdict(存放的数据类型)**

```python
d = defaultdict()
print(d)
# defaultdict(None, {})
e = defaultdict(str)
print(e)
# defaultdict(<class 'str'>, {})
```

defaultdict的一个典型用法是使用其中一种内置类型(如str、int、list或dict)作为默认工厂，因为这些内置类型在没有参数调用时返回空类型。

```python
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
```

使用`int`作为default_factory的例子：

```python
fruit = defaultdict(int)
fruit['apple'] += 2 
print(fruit)    # defaultdict(<class 'int'>, {'apple': 2})
fruit['apple'] += 2 
print(fruit)    # defaultdict(<class 'int'>, {'apple': 4})

# 没有对象时，返回0
print(fruit['banana'])
print(fruit)    # defaultdict(<class 'int'>, {'apple': 4, 'banana': 0})
```

使用`list`作为default_factory的例子：

```python
s = [('NC', 'Raleigh'), ('VA', 'Richmond'), ('WA', 'Seattle'), ('NC', 'Asheville')]

# dict存放的数据类型是list
d = defaultdict(list)
for k, v in s:
    d[k].append(v)
print(d)
# defaultdict(<class 'list'>, {'NC': ['Raleigh', 'Asheville'], 'VA': ['Richmond'], 'WA': ['Seattle']})
```

## OrderedDict 保存添加顺序

Python字典中的键的顺序是任意的:它们不受添加的顺序的控制。
 `collections.OrderedDict `类提供了保留他们添加顺序的字典对象。

```python
'''
Python字典中的键的顺序是任意的:它们不受添加的顺序的控制。
`collections.OrderedDict `类提供了保留他们添加顺序的字典对象。
如果在已经存在的key上添加新的值，将会保留原来的key的位置，然后覆盖value值。
'''

from collections import OrderedDict


o = OrderedDict()

o['key2'] = 'value2'
o['key1'] = 'value1'
o['key3'] = 'value3'
print(o)
# OrderedDict([('key2', 'value2'), ('key1', 'value1'), ('key3', 'value3')])

```

如果在已经存在的key上添加新的值，将会保留原来的key的位置，然后覆盖value值。

```python
o['key1'] = 'value4'
print(o)
# OrderedDict([('key2', 'value2'), ('key1', 'value4'), ('key3', 'value3')])
```

## namedtuple 命名元组,像对象一样

三种定义命名元组的方法：第一个参数是命名元组的构造器（如下的：Person，Human）, 三种效果完全一样

```python
'''
命名元组,像对象一样

'''

from collections import namedtuple

# 三种定义命名元组的方法：第一个参数是命名元组的构造器（如下的：Person，Human） 效果完全一样
Person = namedtuple('Person', ['age', 'height', 'name'])
Human  = namedtuple('Human', 'age, height, name')
Human2 = namedtuple('Human2', 'age height name')
```

实例化命令元组

```python
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
```





## deque 双向队列

`collections.deque`返回一个新的双向队列对象，从左到右初始化(用方法 append()) ，从 iterable （迭代对象) 数据创建。如果 iterable 没有指定，新队列为空。
 `collections.deque`队列支持线程安全，对于从两端添加(append)或者弹出(pop)，复杂度O(1)。
 虽然`list`对象也支持类似操作，但是这里优化了定长操作（pop(0)、insert(0,v)）的开销。
 如果 maxlen 没有指定或者是 None ，deques 可以增长到任意长度。否则，deque就限定到指定最大长度。一旦限定长度的deque满了，当新项加入时，同样数量的项就从另一端弹出。

> 方法：

- append(x)：添加x到右端

- appendleft(x)：添加x到左端



- insert(i,x)：在位置 i 插入 x 。注：如果插入会导致一个限长deque超出长度 maxlen 的话，就升起一个 IndexError 。



- extend(iterable)：在队列右侧添加iterable中的元素

- extendleft(iterable)：在队列左侧添加iterable中的元素，注：在左侧添加时，iterable参数的顺序将会反过来添加(右->左)



- pop()：移除最右侧的元素

- popleft()：移除最左侧的元素



- remove(value)：*移去找到的第一个value(左->右)。没有抛出ValueError*

- clear()：清楚所有元素，长度变为0



- copy()：创建一份浅拷贝,*虽然是浅拷贝,但是一个添加值,另一个不会变*

- count(x)：计算队列中个数等于x的元素



- index(x[,start[,stop]])：返回第 x 个元素下标（从 start 开始计算，在 stop 之前）。返回第一个匹配，如果没找到的话，升起 ValueError 。



- reverse()：将deque逆序排列。返回 None 。

> 属性

- maxlen：队列的最大长度，没有限定则为None。



```python
'''
`collections.deque`返回一个新的双向队列对象，从左到右初始化(用方法 append()) ，
从 iterable （迭代对象) 数据创建。如果 iterable 没有指定，新队列为空。
`collections.deque`队列支持线程安全，对于从两端添加(append)或者弹出(pop)，复杂度O(1)。
虽然`list`对象也支持类似操作，但是这里优化了定长操作（pop(0)、insert(0,v)）的开销。
如果 maxlen 没有指定或者是 None ，deques 可以增长到任意长度。
否则，deque就限定到指定最大长度。一旦限定长度的deque满了，当新项加入时，同样数量的项就从另一端弹出。

    - append(x)：添加x到右端
    - appendleft(x)：添加x到左端

    - insert(i, x)：在位置 i 插入 x 。注：如果插入会导致一个限长deque超出长度 maxlen 的话，就升起一个 IndexError 。
    
    - extend(iterable)：在队列右侧添加iterable中的元素
    - extendleft(iterable)：在队列左侧添加iterable中的元素，注：在左侧添加时，iterable参数的顺序将会反过来添加(右->左)

    - pop()：移除最右侧的元素
    - popleft()：移除最左侧的元素

    - remove(value)：移去找到的第一个value(左->右)。没有抛出ValueError
    - clear()：清楚所有元素，长度变为0

    - copy()：创建一份浅拷贝,虽然是浅拷贝,但是一个添加值,另一个不会变
    - count(x)：计算队列中个数等于x的元素

    - index(x[,start[,stop]])：返回第 x 个元素（从 start 开始计算，在 stop 之前）。返回第一个匹配，如果没找到的话，升起 ValueError 。
    
    - reverse()：将deque逆序排列。返回 None 。
    - maxlen：队列的最大长度，没有限定则为None。
'''

from collections import deque

d = deque(maxlen=10)


# append(x),appendleft(x)：添加到左右两端
d.append('a')
d.append('b')
d.appendleft('e')
d.appendleft('f')
d.appendleft('e')
print(d)    # deque(['e', 'f', 'e', 'a', 'b'], maxlen=10)
print('~' * 50)


# insert(i,x)：在位置 i 插入 x 。注：如果插入会导致一个限长deque超出长度 maxlen 的话，就升起一个 IndexError 。
d.insert(0, 'x')
print(d)    # deque(['x', 'e', 'f', 'e', 'a', 'b'], maxlen=10)
print('~' * 50)


# extend(iterable),extendleft(iterable)：扩展新的列表
d.extend('mn')
print(d)    # deque(['x', 'e', 'f', 'e', 'a', 'b', 'm', 'n'], maxlen=10)
d.extendleft('oi')
print(d)    # deque(['i', 'o', 'x', 'e', 'f', 'e', 'a', 'b', 'm', 'n'], maxlen=10)
print('~' * 50)


# pop,popleft：左右出栈
res = d.pop()
print(res)  # n
res = d.popleft()
print(res)  # i
print(d)    # deque(['o', 'x', 'e', 'f', 'e', 'a', 'b', 'm'], maxlen=10)
print('~' * 50)


# remove(value)：移去找到的第一个value(左->右)。没有抛出ValueError
d.remove('e')                     # 从左
print(d)    # deque(['o', 'x', 'f', 'e', 'a', 'b', 'm'], maxlen=10)
print('~' * 50)


# clear()：清除全部
d.clear()
print(d)    # deque([], maxlen=10)
print('~' * 50)


# copy()：浅拷贝
d.extend('aidkmadad')
dd = d.copy()
d.append('m')
print(d)
print(dd)
# 虽然是浅拷贝,但是一个添加值,另一个不会变
# deque(['a', 'i', 'd', 'k', 'm', 'a', 'd', 'a', 'd', 'm'], maxlen=10)
# deque(['a', 'i', 'd', 'k', 'm', 'a', 'd', 'a', 'd'], maxlen=10)
print('~' * 50)


# count(x)：计算队列中个数等于x的元素
print(d.count('a')) # 3
print('~' * 50)


# index(x[,start[,stop]])：返回第 x 个元素下标（从 start 开始计算，在 stop 之前）。返回第一个匹配，如果没找到的话，升起 ValueError 。
print(d.index('a')) # 0
print('~' * 50)


# reverse()：将deque逆序排列。返回 None 。
print(d) 
d.reverse()
print(d) 
# deque(['a', 'i', 'd', 'k', 'm', 'a', 'd', 'a', 'd', 'm'], maxlen=10)
# deque(['m', 'd', 'a', 'd', 'a', 'm', 'k', 'd', 'i', 'a'], maxlen=10)
print('~' * 50)


# maxlen：属性 队列的最大长度，没有限定则为None。
print(d.maxlen) # 10
```

## ChainMap 将多个字典放到一起,不过不会形成新的字典,但可以使用字典的操作

一个 ChainMap 将多个字典或者其他映射组合在一起，创建一个单独的可更新的视图。 如果没有 maps 被指定，就提供一个默认的空字典 。`ChainMap`是管理嵌套上下文和覆盖的有用工具。

```python
'''
拼接多个字典到一起
一个 ChainMap 将多个字典或者其他映射组合在一起，创建一个单独的可更新的视图。 
如果没有 maps 被指定，就提供一个默认的空字典 。`ChainMap`是管理嵌套上下文和覆盖的有用工具。

'''

from collections import ChainMap



d1 = {'apple':1,'banana':2}
d2 = {'orange':2,'apple':3,'pike':1}
combined_d = ChainMap(d1, d2)
reverse_combined_d = ChainMap(d2, d1)

print(combined_d)
print(reverse_combined_d)
# ChainMap({'apple': 1, 'banana': 2}, {'orange': 2, 'apple': 3, 'pike': 1})
# ChainMap({'orange': 2, 'apple': 3, 'pike': 1}, {'apple': 1, 'banana': 2})


# 重复的键不会多次获取
for k, v in combined_d.items():
    print(k, v) 
    # apple 1
    # pike 1
    # banana 2
    # orange 2
print('-' * 50)


for k, v in reverse_combined_d.items():
    print(k, v) 
    # orange 2
    # banana 2
    # apple 3
    # pike 1
```