# starmap, 类似 map, 但是接受多个参数的元组作为输入, 并将其映射到函数的多个参数上, 返回的是包含函数结果的迭代器.


from itertools import starmap


def get_sum(*args: int) -> int:
    return sum(args)


data: list[tuple[int, int, int]] = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
sums: starmap = starmap(get_sum, data)
print(list(sums))
# [6, 15, 24]


data: list[tuple[int, int]] = [(2, 4), (3, 3), (4, 2)]
pows: starmap = starmap(pow, data)
print(list(pows))
# [16, 27, 16]
