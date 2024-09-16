from typing import Callable

"""
Callable 表示可调用的
"""


def my_func1(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        print("start")
        res = func(*args, **kwargs)
        print("end")
        return res

    return wrapper


@my_func1
def func1(*args, **kwargs):
    print("func1")
    return 1


func1()


"""
Callable[[int, int], int]
前面的类型代表输入值,后面的类型代表输出值
代表 输入值是2个 int, 返回值是一个 int
"""


def my_func2(func: Callable[[int, int], int]) -> Callable:
    def wrapper(a: int, b: int):
        print("args: ", a, b)
        res = func(a, b)
        print("res: ", res)
        return res

    return wrapper


@my_func2
def func2(a: int, b: int) -> int:
    return a + b


func2(1)
