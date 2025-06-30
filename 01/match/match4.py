# match cast with if statement


def match_quadrant(point):
    match point:
        case (x, y) if x > 0 and y > 0:
            print("First quadrant")
        case (x, y) if x < 0 and y > 0:
            print("Second quadrant")
        case (x, y) if x < 0 and y < 0:
            print("Third quadrant")
        case (x, y) if x > 0 and y < 0:
            print("Fourth quadrant")
        case (x, y):
            print("On an axis or at the origin")
        case ():
            print("Empty point")
        case _:
            print("Not a valid point")


match_quadrant((1, 1))  # First quadrant
match_quadrant((-1, 1))  # Second quadrant
match_quadrant((-1, -1))  # Third quadrant
match_quadrant((1, -1))  # Fourth quadrant
match_quadrant((0, 0))  # On an axis or at the origin
match_quadrant((1, 0))  # On an axis or at the origin
match_quadrant([])  # Empty point
match_quadrant(())  # Empty point
match_quadrant((0, 1, 2))  # Not a valid point
