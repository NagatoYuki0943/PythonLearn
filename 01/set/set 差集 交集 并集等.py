a: set = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
b: set = set([4, 5, 6, 7, 8, 9, 10, 11, 12])


# 返回集合的交集
print(a.intersection(b))  # {4, 5, 6, 7, 8, 9}
print(a & b)  # {4, 5, 6, 7, 8, 9}


# 返回两个集合的并集
print(a.union(b))  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
print(a | b)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}


# 返回多个集合的差集
# 顺序有差别
print(a.difference(b))  # {1, 2, 3}
print(a - b)  # {1, 2, 3}

print(b.difference(a))  # {10, 11, 12}
print(b - a)  # {10, 11, 12}


# 返回两个集合中不重复的元素集合(不同时包含于a和b的元素)
# 差集的并集
print(a.symmetric_difference(b))  # {1, 2, 3, 10, 11, 12}
print(a ^ b)  # {1, 2, 3, 10, 11, 12}
print("*" * 100)


# 判断两个集合是否不相交, 不相交返回 True, 否则返回 False
print(a.isdisjoint(b))  # False
c = set([1, 2, 3])
print(a.isdisjoint(c))  # False
d = set([10, 11, 12])
print(a.isdisjoint(d))  # True


# a 是否为 b 的子集, 即 a 中的元素都在 b 中, 如果是返回 True, 否则返回 False
print(a.issubset(b))  # False
print(c.issubset(a))  # True
print(a.issubset(a))  # True


# a 是否为 b 的超集, 即 b 中的元素都在 a 中, 如果是返回 True, 否则返回 False
print(b.issuperset(a))  # False
print(a.issuperset(c))  # True
print(a.issuperset(a))  # True
print("*" * 100)


# 空集操作
empty_set1 = set()
empty_set2 = set()
print(empty_set1.intersection(empty_set2))  # set()
print(empty_set1.union(empty_set2))  # set()
print(empty_set1.difference(empty_set2))  # set()
print(empty_set1.symmetric_difference(empty_set2))  # set()
print(empty_set1.isdisjoint(empty_set2))  # True
print(empty_set1.issubset(empty_set2))  # True
print(empty_set1.issuperset(empty_set2))  # True
