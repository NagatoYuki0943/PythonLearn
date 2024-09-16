"""
filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的对象,使用list转换。
该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判断，
然后返回 True 或 False，最后将返回 True 的元素放到新列表中。


filter() 方法的语法:
    filter(function, iterable)

参数
    function -- 判断函数。
    iterable -- 可迭代对象。


filter和map参数1都是函数,参数2是列表
"""

import torch


def is_odd(n):
    return n % 2 == 1


newlist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(list(newlist))
print("*" * 50)

t = torch.randn(4, 1)
res = filter(lambda x: x > 0, t)

print(torch.tensor(list(res)))
# tensor([0.5339, 0.1579])
