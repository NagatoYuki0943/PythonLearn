"""
yeild 迭代器可以被返回
yield from 后面加上可迭代对象，他可以把可迭代对象里的每个元素一个一个的yield出来，
对比yield来说代码更加简洁，结构更加清晰。
"""


def number():
    # 从一个可迭代对象中生成一个迭代器
    yield from [f'<< {i}' for i in range(4)]

for i in number():
    print(i, end=" ")
print()
# << 0 << 1 << 2 << 3


def reader():
    for i in range(4):
        yield f'<< {i}'


def reader_wrapper1():
    # Instead of manually iterating over reader(), we can just yield from it.
    yield from reader()

wrap = reader_wrapper1()
for i in wrap:
    print(i, end=" ")
print()
# << 0 << 1 << 2 << 3


def reader_wrapper2():
    # 直接返回 reader() 的迭代器,效果和 yield from 一样
    return reader()

wrap = reader_wrapper2()
for i in wrap:
    print(i, end=" ")
print()
# << 0 << 1 << 2 << 3
