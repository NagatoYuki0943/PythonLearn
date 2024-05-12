from typing import Literal

"""
Literal 代表字面意思必须是这样的,类似 Enum
"""


# 将类型专门作为 Literal 类型传入
GenderType = Literal["male", "female"]


class Person:
    def __init__(
        self,
        name: str,
        gender: GenderType
    ) -> None:
        self.name = name
        self.gender = gender


a = Person("Tom", "male")
b = Person("Jerry", "female")
c = Person("Duck", "woman") # 无法通过检查

# 但是将字符串类型当做 Literal 类型传入会无法通过检查
# 因为 gender 类型是 string,不符合 Literal["male", "female"]
# 需要也可以 gender 标注类型才行
gender: GenderType = "male"
d = Person("Dog", gender)
