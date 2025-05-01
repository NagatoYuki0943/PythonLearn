# 无限迭代器（Infinite Iterators）
# repeat(elem [,n])是将一个元素重复n遍或者无穷多遍，并返回一个迭代器


from itertools import repeat
import time


for i in repeat(1, 3):
    print(i)
# 1
# 1
# 1

print(list(repeat(1, 3)))
# [1, 1, 1]

print(list(repeat([1, 2], 3)))
# [[1, 2], [1, 2], [1, 2]]

for i in repeat(1):
    print(i)
    time.sleep(1)
