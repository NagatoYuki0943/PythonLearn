from typing import TypeVar


T = TypeVar("T", int, float, str)


# 代表 x, y, 返回值可以是 int, float, str 类型, 但必须同时是一种类型
def add1(x: T, y: T) -> T:
    return x + y


print(add1(1, 2))  # Output: 3
print(add1(1.5, 2.5))  # Output: 4.0
print(add1("hello", " world"))  # Output: hello world


# 3.12 支持简化语法
def add2[T: (int, float, str)](x: T, y: T) -> T:
    return x + y


print(add2(1, 2))  # Output: 3
print(add2(1.5, 2.5))  # Output: 4.0
print(add2("hello", " world"))  # Output: hello world
