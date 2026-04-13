from typing import TypeAlias, Annotated
import numpy as np
import torch
from pydantic import BaseModel, Field


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


type array = np.ndarray | torch.Tensor


def add(a: array, b: array) -> array: ...


# type 配合 Annotated 定义带有注释的类型
type Name = Annotated[str, Field(min_length=3, max_length=64), "姓名"]
type Age = Annotated[int, Field(gt=0), "必须大于0"]

# 结合泛型 [T] 和 Annotated，定义一个最大长度为 5 的泛型列表
type Max5List[T] = Annotated[list[T], Field(max_length=5), "最多包含5个元素"]


class UserProfile(BaseModel):
    name: Name
    age: Age

    # 这是一个最多包含 5 个字符串的列表
    hobbies: Max5List[str]

    # 这是一个最多包含 5 个整数的列表
    lucky_numbers: Max5List[int]
