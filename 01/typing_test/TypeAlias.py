

# 类型作为别名
ReturnType = tuple[int, str | None]


def f(x: int) -> ReturnType:
    if x > 0:
        print(x)
        return (0, None)
    else:
        return (0, "Negative")


retcode, errmsg = f(1)
print(retcode, errmsg)
retcode, errmsg = f(-1)
print(retcode, errmsg)
