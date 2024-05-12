from typing import Sequence


# 如果一个函数想传递 list 或者 tuple,可以使用 Sequence 作为 type hint
def my_sum(lst: Sequence[int]) -> int:
    total = 0
    for i in lst:
        total += i
    return total


my_sum([0, 1, 2])
my_sum((0, 1, 2))
