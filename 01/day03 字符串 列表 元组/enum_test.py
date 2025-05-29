from enum import Enum, IntEnum, StrEnum, auto
from beartype import beartype


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

    @classmethod
    def print_color(cls):
        for color in cls:
            # 每个枚举值都有 name 和 value 属性
            print(color.name, color.value)


Color.print_color()
print()
# RED 1
# GREEN 2
# BLUE 3

print(Color.RED) # Color.RED
print(Color.RED == 1) # False 这里看到它和 1 不相等
print(Color.RED.value == 1) # True
print()


@beartype
def func(color: Color) -> str:
    if color == Color.RED:
        return "Red"
    elif color == Color.GREEN:
        return "Green"
    elif color == Color.BLUE:
        return "Blue"
    else:
        raise ValueError("Unknown color")


print(func(Color.RED))  # Red
print("*" * 100)


# 相当于同时继承 Int 和 Enum
class Color1(IntEnum):
    RED = 1
    GREEN = 2
    BLUE = 3

    @classmethod
    def print_color(cls):
        for color in cls:
            # 每个枚举值都有 name 和 value 属性
            print(color.name, color.value)


Color1.print_color()
print()
# RED 1
# GREEN 2
# BLUE 3

print(Color1.RED) # 1
print(Color1.RED == 1) # True 这里看到它和 1 相等
print(Color1.RED.value == 1) # True
print("*" * 100)


# 相当于同时继承 Str 和 Enum
class Color2(StrEnum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"

    @classmethod
    def print_color(cls):
        for color in cls:
            # 每个枚举值都有 name 和 value 属性
            print(color.name, color.value)


Color2.print_color()
print()
# RED red
# GREEN green
# BLUE blue

print(Color2.RED) # red
print(Color2.RED == "red") # True
print("*" * 100)


# 不在乎存储的什么值, Enum 或者 Enum 数字从 0 开始， StrEnum 字符串自动把前面的变量名改为小写
class Color3(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()

    @classmethod
    def print_color(cls):
        for color in cls:
            # 每个枚举值都有 name 和 value 属性
            print(color.name, color.value)


Color3.print_color()
print()
# RED 1
# GREEN 2
# BLUE 3

print(Color3.RED) # 1
print(Color3.RED == 1) # False
print(Color3.RED.value == 1) # True
print("*" * 100)
