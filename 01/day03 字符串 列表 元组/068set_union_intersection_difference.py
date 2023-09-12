"""set可以用来求交集,并集,差集和补集
"""


x = {1, 2, 3, 4}
y = {3, 4, 5, 6}


# 求交集 返回一个新的集合，包括同时在集合 x 和y中的共同元素。
print(x.intersection(y))            # {3, 4}
print(y.intersection(x))            # {3, 4}
print(x & y)                        # {3, 4}
print(y & x)                        # {3, 4}


# 求并集 返回一个新的集合，包括集合 x 和 y 中所有元素。
print(x.union(y))                   # {1, 2, 3, 4, 5, 6}
print(y.union(x))                   # {1, 2, 3, 4, 5, 6}
print(x | y)                        # {1, 2, 3, 4, 5, 6}
print(y | x)                        # {1, 2, 3, 4, 5, 6}


# 求差集 返回一个新的集合,包括在集合 x(y) 中但不在集合 y(x) 中的元素。
print(x.difference(y))              # {1, 2}
print(x - y)                        # {1, 2}
print(y.difference(x))              # {5, 6}
print(y - x)                        # {5, 6}


# 求补集 返回一个新的集合，包括集合 x 和 y 的非共同元素。
print(x.symmetric_difference(y))    # {1, 2, 5, 6}
print(y.symmetric_difference(x))    # {1, 2, 5, 6}
print(x ^ y)                        # {1, 2, 5, 6}
print(y ^ x)                        # {1, 2, 5, 6}

