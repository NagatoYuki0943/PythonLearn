# 组合迭代器（Combinatoric Iterators）
# permutations(iterable,r=None)返回的是可迭代元素中的一个排列组合，
# 并且是按顺序返回的，且不包含重复的结果


from itertools import permutations


for i in permutations([0, 1]):
    print(i)
print("\n")
# (0, 1)
# (1, 0)


for i in permutations([0, 1, 2]):
    print(i)
print("\n")
# (0, 1, 2)
# (0, 2, 1)
# (1, 0, 2)
# (1, 2, 0)
# (2, 0, 1)
# (2, 1, 0)


# 注意：permutations函数当迭代对象出现相同元素时，是会产生重复结果
for i in permutations([0, 0]):
    print(i)
print("\n")
# (0, 0)
# (0, 0)


# 第 2 个参数默认为None，它表示的是返回元组（tuple) 的长度
for i in permutations([0, 1], r=1):
    print(i)
print("\n")
# (0,)
# (1,)


# 第 2 个参数默认为None，它表示的是返回元组（tuple) 的长度
for i in permutations([0, 1], r=2):
    print(i)
print("\n")
# (0, 1)
# (1, 0)
