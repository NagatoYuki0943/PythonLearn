from typing import Any, NoReturn


# 当函数没有显示返回值时,默认其实是返回了 None
def f1(x: Any):
    ...

res = f1(1)
print(res)  # None


# 真正的没有返回值,比如 raise error 或者 exit,可以使用 NoReturn 作为返回值
def f2(x: Any) -> NoReturn:
    # raise Exception
    exit()


f2(1)
print("A") # 代码无法访问
