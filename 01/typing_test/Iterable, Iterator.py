from typing import Iterable, Iterator
"""
Python中的Iterable和Iterator是两个不同的概念,但它们都与迭代有关。

Iterable:
    - Iterable是一个可以产生迭代器(Iterator)的对象。换句话说,如果一个对象实现了__iter__方法,它就可以被视为一个Iterable。
    - Iterable对象定义了一个迭代的序列,但是Iterable本身不能被迭代,只能通过生成一个Iterator来进行迭代。
    - 常见的Iterable对象包括列表(list)、元组(tuple)、字符串(str)、字典(dict)等。

Iterator:
    - Iterator是一个可以记住遍历序列中的位置的对象。它可以在你调用next()方法时返回序列中的下一个元素。
    - Iterator实现了两个方法:__iter__()和__next__()。__iter__()返回迭代器本身,__next__()返回迭代器中的下一个值。
    - 当序列中没有更多的元素时,__next__()方法会引发StopIteration异常。
    - 可以使用内置函数iter()将一个Iterable对象转换为一个Iterator对象。
"""


# Iterable
my_list = [1, 2, 3]
print(isinstance(my_list, Iterable))  # True


# Iterator
my_iter = iter(my_list)
print(isinstance(my_iter, Iterator))  # True
print(next(my_iter))  # 1
print(next(my_iter))  # 2
print(next(my_iter))  # 3
print(next(my_iter))  # 引发 StopIteration 异常
