from dataclasses import dataclass

class Point1:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point1(10, 20)


match p:
    case Point1(x=0, y=0):
        print("Origin")
    case Point1(x=0, y=y):
        print(f"On Y-axis at {y}")
    # case 里面必须使用关键字参数
    case Point1(x=x, y=0):
        print(f"On X-axis at {x}")
    case Point1(x=x, y=y):
        print(f"Point1 at ({x}, {y})")
    case _:
        print("Unknown Point1")
# Point1 at (10, 20)


# 如果想在 case 中使用位置参数，要添加 __match_args__ 指定位置参数
class Point2:
    __match_args__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point2(10, 20)


match p:
    case Point2(0, 0):
        print("Origin")
    case Point2(0, y):
        print(f"On Y-axis at {y}")
    # case 里面必须使用关键字参数
    case Point2(x, 0):
        print(f"On X-axis at {x}")
    case Point2(x, y):
        print(f"Point2 at ({x}, {y})")
    case _:
        print("Unknown Point2")
# Point2 at (10, 20)


# 如果使用的是 dataclass，可以直接使用位置参数
@dataclass
class Point3:
    x: int
    y: int


p = Point3(10, 20)


match p:
    case Point3(0, 0):
        print("Origin")
    case Point3(0, y):
        print(f"On Y-axis at {y}")
    # case 里面必须使用关键字参数
    case Point3(x, 0):
        print(f"On X-axis at {x}")
    case Point3(x, y):
        print(f"Point3 at ({x}, {y})")
    case _:
        print("Unknown Point3")
# Point3 at (10, 20)
