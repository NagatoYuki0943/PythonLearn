from typing import Any
import math

# Any 任意类型

def f1(x: int | float) -> Any:
    return math.sqrt(x)

print(f1(4))    # 2.0
print(f1(2))    # 1.4142135623730951

