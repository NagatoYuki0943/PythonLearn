dict_p = {"x": 20, "y": 30}


match dict_p:
    case {"x": 0, "y": 0}:
        print("Origin")
    case {"x": 0, "y": y}:
        print(f"On Y-axis at {y}")
    case {"x": x, "y": 0}:
        print(f"On X-axis at {x}")
    case {"x": x, "y": y}:
        print(f"Point at ({x}, {y})")
    case _:
        print("Unknown point")
# Point at (20, 30)


match dict_p:
    case {"x": 20, "y": 30}:
        print("Matched")
# Matched


match dict_p:
    case {"x": 20}:
        print("Matched")
# Matched


match dict_p:
    case {"y": 30}:
        print("Matched")
# Matched
