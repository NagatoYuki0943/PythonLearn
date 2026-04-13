from typing import TypeAlias
import numpy as np
import torch


# 最简单的写法
Url1 = str

def retry1(url: Url1, retry_count: int) -> None: ...


# 使用 TypeAlias 定义类型别名
Url2: TypeAlias = str
array: TypeAlias = np.ndarray | torch.Tensor

def retry2(url: Url2, retry_count: int) -> None: ...


# 3.12 and later, 使用 type 定义类型别名
type Url3 = str
type array = np.ndarray | torch.Tensor

def retry3(url: Url3, retry_count: int) -> None: ...
