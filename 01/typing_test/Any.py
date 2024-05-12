from typing import Any
import math


# Any 任意类型,在不进行 type hint 时,默认类型为 Any
def f1(x: Any) -> Any:
    return x


print(f1(4))    # 2.0
print(f1("a"))  # 2.0

