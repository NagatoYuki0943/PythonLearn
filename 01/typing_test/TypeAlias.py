from typing import TypeAlias, Annotated
import numpy as np
import torch
from pydantic import Field


# 最简单的写法
Url1 = str

def retry1(url: Url1, retry_count: int) -> None: ...


# 使用 TypeAlias 定义类型别名
Url2: TypeAlias = str
array: TypeAlias = np.ndarray | torch.Tensor

def retry2(url: Url2, retry_count: int) -> None: ...


# 3.12 and later, 使用 type 定义类型别名
type Url3 = str

def retry3(url: Url3, retry_count: int) -> None: ...

# 其他用法
type array = np.ndarray | torch.Tensor
# type 配合 Annotated 定义带有注释的类型
type Age = Annotated[int, "必须大于0"]
# 结合泛型 [T] 和 Annotated，定义一个最大长度为 5 的泛型列表
type Max5List[T] = Annotated[list[T], Field(max_length=5)]
