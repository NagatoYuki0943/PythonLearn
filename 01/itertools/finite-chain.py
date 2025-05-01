# 有限迭代器（Iterators Terminating on the Shortest Input Sequence）
# chain(*iterables) 可以把多个可迭代对象组合起来，形成一个更大的迭代器


from itertools import chain


for i in chain(
    [
        1,
        2,
        3,
    ],
    ["A", "B"],
):
    print(i)
print("\n")
# 1
# 2
# 3
# A
# B


for i in chain("good", "bye"):
    print(i)
print("\n")
# g
# o
# o
# d
# b
# y
# e
