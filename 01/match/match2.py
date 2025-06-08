def if_point(point):
    if len(point) == 2:
        if point[0] == 0 and point[1] == 0:
            print("Origin")
        else:
            print(f"x={point[0]}, y={point[1]}")
    else:
        print(f"Invalid point: {point}")


if_point((0, 0))  # Origin
if_point((1, 2))  # x=1, y=2
if_point((0, 0, 0))  # Invalid point: (0, 0, 0)
print()


def match_point1(point):
    match point:
        case (0, 0):
            print("Origin")
        case (x, 0):
            print(f"on x-axis, {x=}")
        case (0, y):
            print(f"on y-axis, {y=}")
        case (x, y):
            print(f"{x=}, {y=}")
        # 这里最后一个就是默认值
        # case other:
        case _:
            print(f"Invalid point: {point}")


match_point1((0, 0))  # Origin
match_point1((1, 0))  # on x-axis, x=1
match_point1((0, 2))  # on y-axis, y=2
match_point1((1, 2))  # x=1, y=2
match_point1((0, 0, 0))  # Invalid point: (0, 0, 0)
print()


def match_point2(point):
    match point:
        case (0, 0):
            print("Origin")
        # | 或模式匹配
        case (x, 0) | (0, x):
            print(f"on axis, {x=}")
        case (x, y):
            print(f"{x=}, {y=}")
        # 这里最后一个就是默认值
        # case other:
        case _:
            print(f"Invalid point: {point}")


match_point2((0, 0))  # Origin
match_point2((1, 0))  # on axis, x=1
match_point2((0, 2))  # on axis, x=2
match_point2((1, 2))  # x=1, y=2
match_point2((0, 0, 0))  # Invalid point: (0, 0, 0)
print()
