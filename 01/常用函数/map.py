"""
map() 会根据提供的函数对指定序列做映射。

第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。

map() 函数语法：
    map(function, iterable, ...)
参数
    function -- 函数
    iterable -- 一个或多个序列

map和filter参数1都是函数,参数2是列表
"""


def square(x):
    return x**2


res = list(map(square, [1, 2, 3, 4, 5]))
print(res)
# [1, 4, 9, 16, 25]

result = list(map(lambda x: x**2, [1, 2, 3, 4, 5]))
print(result)
# [1, 4, 9, 16, 25]
