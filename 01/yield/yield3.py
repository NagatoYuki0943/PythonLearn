"""
yield from后面加上可迭代对象，他可以把可迭代对象里的每个元素一个一个的yield出来，
对比yield来说代码更加简洁，结构更加清晰。
"""

def reader():
    for i in range(4):
        yield '<< %s' % i

def reader_wrapper1(g):
    # Manually iterate over data produced by reader
    for v in g:
        yield v

wrap = reader_wrapper1(reader())
for i in wrap:
    print(i)
# << 0
# << 1
# << 2
# << 3


def reader_wrapper2(g):
    # Instead of manually iterating over reader(), we can just yield from it.
    yield from g

wrap = reader_wrapper2(reader())
for i in wrap:
    print(i)
# << 0
# << 1
# << 2
# << 3


def reader_wrapper3():
    # Instead of manually iterating over reader(), we can just yield from it.
    yield from reader()

wrap = reader_wrapper3()
for i in wrap:
    print(i)
# << 0
# << 1
# << 2
# << 3
