"""set可以用来求交集,并集和差集
"""


a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# 求交集
print(a.intersection(b))    # {3, 4}
print(b.intersection(a))    # {3, 4}

# 求并集
print(a.union(b))           # {1, 2, 3, 4, 5, 6}
print(b.union(a))           # {1, 2, 3, 4, 5, 6}

# 求差集
print(a.difference(b))      # {1, 2}
print(b.difference(a))      # {5, 6}
