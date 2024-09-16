"""
try:
    # 尝试执行的代码
except Exception as e:
    # 发生异常执行这里的代码
else:
    # 如果没有异常发生，执行这里的代码
finally:
    # 无论是否发生异常，都会执行这里的代码
"""


def func() -> int:
    try:
        raise ValueError("Bad Value")
    except ValueError:
        raise Exception("We not expect this")
        # 这里不管用,还是强制执行finally
        return 1
    finally:
        # 正常运行就返回0
        return 0


print(func())
# 0
