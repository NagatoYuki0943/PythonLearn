# 组合迭代器（Combinatoric Iterators）
# combinations(iterable,r) 返回的是可迭代对象所有的长度为 r 的子序列，
# 与 permutation 不同，permutation 返回的是排列，而 combinations 返回的是组合


from itertools import combinations


for i in combinations([1, 2, 3, 4], r=2):
    print(i)
print("\n")
# (1, 2)
# (1, 3)
# (1, 4)
# (2, 3)
# (2, 4)
# (3, 4)


for i in combinations([1, 2, 3, 4], r=3):
    print(i)
print("\n")
# (1, 2, 3)
# (1, 2, 4)
# (1, 3, 4)
# (2, 3, 4)


for i in combinations([1], r=1):
    print(i)
print("\n")
# (1,)


# 如果 iterable 中元素个数小于 r，则返回空的迭代器
for i in combinations([1], r=2):
    print(i)
print("\n")
