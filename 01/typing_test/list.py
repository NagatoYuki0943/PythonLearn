from typing import List


# list 这个写法是 python3.9 以及以后版本是支持的
def my_sum(lst: list[int]) -> int:
    total = 0
    for i in lst:
        total += i
    return total


my_sum([0, 1, 2])
