# 有限迭代器（Iterators Terminating on the Shortest Input Sequence）
# accumulate(iterable [,func]) 可以计算出一个迭代器，这个迭代器是由特定的二元函数的累计结果生成的，如果不指定的话，默认函数为求和函数


from itertools import accumulate


for i in accumulate([0, 1, 0, 1, 1, 2, 3, 5]):
    print(i)
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
print("\n")


for i in accumulate([0, 1, 0, 1, 1, 2, 3, 5], lambda x, y: x + y):
    print(i)
print("\n")
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13


def my_func(x, y):
    return 2 * x + y


for i in accumulate([0, 1, 0, 1, 1, 2, 3, 5], my_func):
    print(i)
print("\n")
# 0
# 1
# 2
# 5
# 11
# 24
# 51
# 107
