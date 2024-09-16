from typing import Generator, Iterator, Iterable

"""
Generator(生成器)是Python中一种特殊的迭代器。它是一个包含yield关键字的函数,可以暂停和恢复它们自身的执行,从而生成一系列的值。

Generator的特点:
    - 惰性计算: 生成器只有在需要时才会计算下一个值,而不是一次性计算出所有值。这节省了内存空间。
    - 状态保持: 每次yield语句返回一个值后,生成器都会记住它在函数体中的位置,下次调用时会从上次离开的位置继续执行。
    - 可迭代: 生成器是一种特殊的迭代器,可以使用next()函数或在循环中使用。
"""


"""
对于生成器函数的类型注释,我们使用 Iterator 或 Generator 来表示它的返回类型。

Generator[int, None, None] 中的三个类型参数分别表示:
    - int - 生成器生成的元素的类型。
    - None - 在生成器中通过 yield 发送值到生成器的类型,对于普通生成器来说,它不会接收任何值,所以是 None。
    - None - 生成器终止时返回的值的类型,对于普通生成器来说,它不返回任何特殊值,所以也是 None。
"""


def count_up_to1(n: int) -> Generator[int, None, None]:
    i = 0
    while i < n:
        yield i
        i += 1


# 使用生成器
counter = count_up_to1(5)
print(isinstance(counter, Generator))  # True
print(next(counter))  # 0
print(next(counter))  # 1
print(next(counter))  # 2
print(next(counter))  # 3
print(next(counter))  # 4


"""
使用 Iterator 作为函数的返回类型来声明函数的 type hint (mypy不允许)
    - n: int 表示函数参数 n 的类型为 int。
    - -> Iterator[int] 表示函数返回值的类型为一个生成整数的迭代器。
"""


def count_up_to2(n: int) -> Iterator[int]:
    i = 0
    while i < n:
        yield i
        i += 1


# 使用生成器
counter = count_up_to2(5)
print(isinstance(counter, Iterator))  # True
print(next(counter))  # 0
print(next(counter))  # 1
print(next(counter))  # 2
print(next(counter))  # 3
print(next(counter))  # 4


"""
使用 Iterator 作为函数的返回类型来声明函数的 type hint (mypy不允许)
    - n: int 表示函数参数 n 的类型为 int。
    - -> Iterator[int] 表示函数返回值的类型为一个生成整数的迭代器。
"""


def count_up_to3(n: int) -> Iterable[int]:
    i = 0
    while i < n:
        yield i
        i += 1


# 使用生成器
counter = count_up_to3(5)
print(isinstance(counter, Iterable))  # True
print(next(counter))  # 0
print(next(counter))  # 1
print(next(counter))  # 2
print(next(counter))  # 3
print(next(counter))  # 4
