"""
https://www.runoob.com/python/python-func-isinstance.html

isinstance() 与 type() 区别：

    isinstance() 会认为子类是一种父类类型，考虑继承关系。

    type() 不会认为子类是一种父类类型，不考虑继承关系。

如果要判断两个类型是否相同推荐使用 isinstance()。
"""

from torch import nn

model = nn.Conv2d(3, 16, 1)

# 是否是同一个类
print(isinstance(model, nn.Conv2d))  # True
print(type(model) == nn.Conv2d)  # True

# 是否是父类
print(isinstance(model, nn.Module))  # True
print(type(model) == nn.Module)  # False
