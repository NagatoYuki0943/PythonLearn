# 有限迭代器（Iterators Terminating on the Shortest Input Sequence）
# batched(iterable, n),
# 这个函数接受一个可迭代对象iterable和一个整数n，返回一个新的迭代器，将 iterable 划分为大小为 n 的子序列


from itertools import batched


print(list(batched([1, 2], 2)))
print("\n")
# [(1, 2)]


for i in batched(range(7), 2):
    print(i)
print("\n")
# (0, 1)
# (2, 3)
# (4, 5)
# (6,)


for i in batched(range(7), 3):
    print(i)
print("\n")
# (0, 1, 2)
# (3, 4, 5)
# (6,)
