# 组合迭代器（Combinatoric Iterators）
# combinations_with_replacement(iterable, r) 返回一个可与自身重复的元素组合，用法类似于 combinations


from itertools import combinations_with_replacement


for i in combinations_with_replacement([1, 2, 3, 4], r=2):
    print(i)
print("\n")
# (1, 1)
# (1, 2)
# (1, 3)
# (1, 4)
# (2, 2)
# (2, 3)
# (2, 4)
# (3, 3)
# (3, 4)
# (4, 4)


for i in combinations_with_replacement([1, 2, 3, 4], r=3):
    print(i)
print("\n")
# (1, 1, 1)
# (1, 1, 2)
# (1, 1, 3)
# (1, 1, 4)
# (1, 2, 2)
# (1, 2, 3)
# (1, 2, 4)
# (1, 3, 3)
# (1, 3, 4)
# (1, 4, 4)
# (2, 2, 2)
# (2, 2, 3)
# (2, 2, 4)
# (2, 3, 3)
# (2, 3, 4)
# (2, 4, 4)
# (3, 3, 3)
# (3, 3, 4)
# (3, 4, 4)
# (4, 4, 4)


for i in combinations_with_replacement([1], r=1):
    print(i)
print("\n")
# (1,)


for i in combinations_with_replacement([1], r=2):
    print(i)
print("\n")
# (1, 1)
