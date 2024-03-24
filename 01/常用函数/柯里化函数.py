"""
利用嵌套函数可以创建柯里化函数，为可重用的函数调用预先配置某些参数
类似 partial
"""

from typing import Callable
from functools import partial


def multply_setup(a: float) -> Callable:

    def multply(b: float) -> float:
        return a * b

    return multply


multply_2 = multply_setup(2)
multply_3 = multply_setup(3)

print(multply_2(5)) # 10
print(multply_3(5)) # 15
