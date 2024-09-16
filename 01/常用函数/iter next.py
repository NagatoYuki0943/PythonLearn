"""
iter() 函数用来生成迭代器。

next() 返回迭代器的下一个项目。
next() 函数要和生成迭代器的 iter() 函数一起使用。
第一次获取的就是第一条数据
next(iter(data))
"""

import torch


lst = [[1, 2], [3, 4], [5, 6]]

for i in lst:
    print(i)
    # [1, 2]
    # [3, 4]
    # [5, 6]
print("*" * 50)


for i in iter(lst):
    print(i)
    # [1, 2]
    # [3, 4]
    # [5, 6]
print("-" * 50)


tensor = torch.randn(4, 2)
for i in tensor:
    print(i)
    # tensor([ 0.3448, -0.6449])
    # tensor([0.7214, 1.4999])
    # tensor([ 0.3664, -0.0461])
    # tensor([1.5123, 0.3924])
print("*" * 50)


for i in iter(tensor):
    print(i)
    # tensor([ 0.3448, -0.6449])
    # tensor([0.7214, 1.4999])
    # tensor([ 0.3664, -0.0461])
    # tensor([1.5123, 0.3924])
print("-" * 50)


it = iter(tensor)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
# 第一次获取的就是第一条数据
# tensor([ 0.3448, -0.6449])
# tensor([0.7214, 1.4999])
# tensor([ 0.3664, -0.0461])
# tensor([1.5123, 0.3924])
