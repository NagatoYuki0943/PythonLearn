"""
使用一个return 返回多个值,默认返回的元组,可以返回列表,字典等
函数遇到return 就会停止执行,可以直接 return  后面没有任何值,调用返回的是 None,不写返回值也是返回 None
"""


def func(a, b):
    # 返回列表
    return [a + b, a - b]


print(func(4, 5))  # [9, -1]


def func1(a, b):
    # 返回元组
    return a + b, a - b


print(func1(3, 6))  # (9, -3)
res = func1(3, 6)
print(res[0])  # 9
print(res[1])  # -3


def func2(a, b):
    # 返回字典
    return {"sum": a + b, "subtract": a - b}


print(func2(8, 5))  # {'sum': 13, 'subtract': 3}


# 函数遇到return 就会停止执行,可以直接 return  后面没有任何值,调用返回的是 None,不写返回值也是返回 None
def func3():
    a = 10
    return


print(func3())  # None
