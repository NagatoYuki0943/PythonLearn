'''
`collections.deque`返回一个新的双向队列对象，从左到右初始化(用方法 append()) ，
从 iterable （迭代对象) 数据创建。如果 iterable 没有指定，新队列为空。
`collections.deque`队列支持线程安全，对于从两端添加(append)或者弹出(pop)，复杂度O(1)。
虽然`list`对象也支持类似操作，但是这里优化了定长操作（pop(0)、insert(0,v)）的开销。
如果 maxlen 没有指定或者是 None ，deques 可以增长到任意长度。
否则，deque就限定到指定最大长度。一旦限定长度的deque满了，当新项加入时，同样数量的项就从另一端弹出。

方法:
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

属性:
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