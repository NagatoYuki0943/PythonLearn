# namedtuple 是 Python collections 模块中的一个工厂函数，用于创建带字段名的元组子类。
# 它既保留了元组的不可变和轻量特性，又允许通过属性名访问元素，极大提升了代码的可读性和可维护性

from collections import namedtuple
from typing import NamedTuple


# ====================== namedtuple 示例 ====================== #
# 没法编写类型注释，只能通过类型推导

# 定义一个名为 User 的 namedtuple，包含 name, sex, age 三个字段
User = namedtuple('User', ['name', 'sex', 'age'])

# 创建实例
user = User(name='Alice', sex='female', age=30)
print(user)         # User(name='Alice', sex='female', age=30)
print(user.name)    # Alice
print(user[1])      # female

try:
    user.name = 'Bob'
except AttributeError:
    print("can't modify immutable instance")
# can't modify immutable instance


# 字段名可以用列表、元组或空格分隔的字符串传入
# 位置参数或关键字参数都可用于实例化
Point = namedtuple('Point', 'x y')
p = Point(10, 20)
print(p)            # Point(x=10, y=20)
print(p.x, p.y)     # 10 20
# ====================== namedtuple 示例 ====================== #

print("\n")

# ====================== NamedTuple 示例 ====================== #
class User(NamedTuple):
    name: str
    sex: str
    age: int

user = User(name='Alice', sex='female', age=30)
print(user)         # User(name='Alice', sex='female', age=30)
print(user.name)    # Alice
print(user[1])      # female

try:
    user.name = 'Bob'
except AttributeError:
    print("can't modify immutable instance")
# can't modify immutable instance


class Point(NamedTuple):
    x: int
    y: int

p = Point(10, 20)
print(p)            # Point(x=10, y=20)
print(p.x, p.y)     # 10 20

# ====================== NamedTuple 示例 ====================== #
