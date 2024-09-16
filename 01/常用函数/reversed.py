"""
reversed(seq) -> iter 返回的是一个把序列值经过反转之后的迭代器
"""

l = [1, 2, 3, 4]

print(l)  # [1, 2, 3, 4]
print(reversed(l))  # <list_reverseiterator object at 0x000002055CBFACB0>
print(list(reversed(l)))  # [4, 3, 2, 1]

print(list(range(4)))  # [0, 1, 2, 3]
print(list(reversed(range(4))))  # [3, 2, 1, 0]
