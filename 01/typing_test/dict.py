from typing import Dict


# dict 这个写法是 python3.9 以及以后版本是支持的
def my_sum(dic: dict[str, int]) -> int:
    total = 0
    for i in dic.values():
        total += i
    return total


my_sum({"a": 1, "b": 2, "c": 3})

