"""
重复n次
"""

from itertools import repeat


for i in repeat(1, 3):
    print(i)
# 1
# 1
# 1

print(list(repeat(1, 3)))
# [1, 1, 1]

print(list(repeat([1, 2], 3)))
# [[1, 2], [1, 2], [1, 2]]
