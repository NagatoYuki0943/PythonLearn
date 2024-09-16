from typing import Union, Optional


def f1(x: Union[int, None]) -> int:
    if x is None:
        return 0
    return x


f1(None)
f1(1)


# python 3.10 后支持 | 代替 Union
def f2(x: int | None) -> int:
    if x is None:
        return 0
    return x


f2(None)
f2(1)


# Optional[int] 代表这个参数可能是 int 或者 None
def f3(x: Optional[int]) -> int:
    if x is None:
        return 0
    return x


f3(None)
f3(1)
