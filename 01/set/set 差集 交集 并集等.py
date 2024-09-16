a: set = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
b: set = set([4, 5, 6, 7, 8, 9, 10, 11, 12])

# 差集
print(a.difference(b))  # {1, 2, 3}
print(a - b)  # {1, 2, 3}

# 交集
print(a.intersection(b))  # {4, 5, 6, 7, 8, 9}
print(a & b)  # {4, 5, 6, 7, 8, 9}

# 并集
print(a.union(b))  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
print(a | b)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

# 不同时包含于a和b的元素
print(a.symmetric_difference(b))  # {1, 2, 3, 10, 11, 12}
print(a ^ b)  # {1, 2, 3, 10, 11, 12}

# 判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。
print(a.isdisjoint(b))  # False

# 判断指定集合是否为该方法参数集合的子集。
print(a.issubset(b))  # False

# 判断该方法的参数集合是否为指定集合的子集
print(b.issuperset(a))  # False
