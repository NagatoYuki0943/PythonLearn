"""
在函数中定义的局部变量，或者通过计算得出的局部变量， 想要在函数外部访问和使用，此时就可以使用 return 关键字，将这个返回值返回
函数遇到return 就会停止执行,可以直接 return  后面没有任何值,调用返回的是 None,不写返回值也是返回 None
"""


def func(a, b):
    return a + b


print(func(1, 2))


# 函数遇到return 就会停止执行,可以直接 return  后面没有任何值,调用返回的是 None,不写返回值也是返回 None
def func2():
    a = 10
    return


print(func2())  # None
