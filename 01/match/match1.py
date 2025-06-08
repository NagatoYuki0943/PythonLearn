def if_traffic_light(color):
    if color == "red":
        return "stop"
    elif color == "yellow":
        return "wait"
    elif color == "green":
        return "go"
    else:
        return "invalid color"


print(if_traffic_light("red"))  # stop
print(if_traffic_light("yellow"))  # wait
print(if_traffic_light("green"))  # go
print(if_traffic_light("blue"))  # invalid color
print()
# stop
# wait
# go
# invalid color


def match_traffic_light(color):
    match color:
        case "red":
            return "stop"
        case "yellow":
            return "wait"
        case "green":
            return "go"
        case _:
            return "invalid color"


print(match_traffic_light("red"))  # stop
print(match_traffic_light("yellow"))  # wait
print(match_traffic_light("green"))  # go
print(match_traffic_light("blue"))  # invalid color
# stop
# wait
# go
# invalid color
