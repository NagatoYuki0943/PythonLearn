"""
https://docs.python.org/zh-cn/3.13/library/collections.html#deque-objects

deque 对象
class collections.deque([iterable[, maxlen]])
    返回一个新的双向队列对象，从左到右初始化(用方法 append()) ，从 iterable （迭代对象) 数据创建。如果 iterable 没有指定，新队列为空。

    Deque 队列是对栈或 queue 队列的泛化（该名称的发音为 "deck"，是 "double-ended queue" 的简写形式)。 Deque 支持线程安全，高度节省内存地从 deque 的任一端添加和弹出条目，在两个方向上的大致性能均为 O(1)。

    虽然 list 对象也支持类似的操作，但它们是针对快速的固定长度的操作进行优化而 pop(0) 和 insert(0, v) 操作对下层数据表示的大小和位置改变都将产生 O(n) 的内存移动开销。

    如果 maxlen 没有指定或者是 None ，deques 可以增长到任意长度。否则，deque就限定到指定最大长度。一旦限定长度的deque满了，当新项加入时，同样数量的项就从另一端弹出。限定长度deque提供类似Unix filter tail 的功能。它们同样可以用与追踪最近的交换和其他数据池活动。

双向队列(deque)对象支持以下方法：

    append(x)
        添加 x 到右端。

    appendleft(x)
        添加 x 到左端。

    clear()
        移除所有元素，使其长度为0.

    copy()
        创建一份浅拷贝。

    count(x)
        计算 deque 中元素等于 x 的个数。

    extend(iterable)
        扩展deque的右侧，通过添加iterable参数中的元素。

    extendleft(iterable)
        扩展deque的左侧，通过添加iterable参数中的元素。注意，左添加时，在结果中iterable参数中的顺序将被反过来添加。

    index(x[, start[, stop]])
        返回 x 在 deque 中的位置（在索引 start 之后，索引 stop 之前）。 返回第一个匹配项，如果未找到则引发 ValueError。

    insert(i, x)
        在位置 i 插入 x 。
        如果插入会导致一个限长 deque 超出长度 maxlen 的话，就引发一个 IndexError。

    pop()
        移去并且返回一个元素，deque 最右侧的那一个。 如果没有元素的话，就引发一个 IndexError。

    popleft()
        移去并且返回一个元素，deque 最左侧的那一个。 如果没有元素的话，就引发 IndexError。

    remove(value)
        移除找到的第一个 value。 如果没有的话就引发 ValueError。

    reverse()
        将deque逆序排列。返回 None 。

    rotate(n=1)
        向右循环移动 n 步。 如果 n 是负数，就向左循环。
        如果deque不是空的，向右循环移动一步就等价于 d.appendleft(d.pop()) ， 向左循环一步就等价于 d.append(d.popleft()) 。

Deque对象同样提供了一个只读属性:

    maxlen
        Deque的最大尺寸，如果没有限定的话就是 None 。

"""

from collections import deque

# 新建一个包含三项的双端队列
d = deque("ghi")

# 迭代双端队列的元素
for elem in d:
    print(elem.upper())
# G
# H
# I

# 添加一个新条目到右端
d.append("j")
print(d)
# deque(['g', 'h', 'i', 'j'])

# 添加一个新条目到左端
d.appendleft("f")
print(d)
# deque(['f', 'g', 'h', 'i', 'j'])

# 一次添加多个元素
d.extend("jk")
print(d)
# deque(['f', 'g', 'h', 'i', 'j', 'j', 'k'])

# 一次添加多个元素到左端
d.extendleft("ab")
print(d)
# deque(['b', 'a', 'f', 'g', 'h', 'i', 'j', 'j', 'k'])

# 计算元素出现的次数
print(d.count("j"))
# 2

# 计算元素的索引
print(d.index("h"))
# 4

# 移去右端的元素
print(d.pop())
# k

# 移去左端的元素
print(d.popleft())
# b

# 移除第一个出现的元素
d.remove("j")
print(d)
# deque(['a', 'f', 'g', 'h', 'i', 'j'])

# 在索引2处插入元素x
d.insert(2, "x")
print(d)
# deque(['a', 'f', 'x', 'g', 'h', 'i', 'j'])

# 反向列出双端队列的内容
print(list(reversed(d)))
# ['j', 'i', 'h', 'g', 'x', 'f', 'a']

# 新建一个反向的双端队列
print(deque(reversed(d)))
# deque(['j', 'i', 'h', 'g', 'x', 'f', 'a'])

# 逆序排列
d.reverse()
print(d)
# deque(['j', 'i', 'h', 'g', 'x', 'f', 'a'])

# 向右循环移动一步
d.rotate(1)
print(d)
# deque(['a', 'j', 'i', 'h', 'g', 'x', 'f'])

# 向左循环移动一步
d.rotate(-1)
print(d)
# deque(['j', 'i', 'h', 'g', 'x', 'f', 'a'])

# 创建一份浅拷贝
d1 = d.copy()
print(d1)
# deque(['j', 'i', 'h', 'g', 'x', 'f', 'a'])

# 清空双端队列
d.clear()
print(d)
# deque([])
