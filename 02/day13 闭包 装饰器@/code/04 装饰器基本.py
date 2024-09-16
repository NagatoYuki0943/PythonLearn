"""
给login函数增加验证功能,不能修改源代码
将login函数传递给外部函数,在内部函数中使用它,还可以添加新功能

# 装饰器,先调用 不用手动调用闭包了
@ function_out  <--  闭包外层函数名
def login():
    print('----开始登陆----')

"""


def login():
    print("----开始登陆----")


login()
# ----开始登陆----
print("*" * 50)


def function_out(func):
    def function_in():
        print("----开始验证----")
        # 调用login
        func()

    return function_in


# 手动调用闭包
# 通过闭包调用函数
login = function_out(login)
login()
# ----开始验证----
# ----开始登陆----
print("*" * 50)


# 不赋值给变量直接调用就会多打印一行
function_out(login)()
# ----开始验证----
# ----开始验证----
# ----开始登陆----
print("*" * 50)


# 装饰器,不用手动调用闭包了
# @外层函数名
@function_out
def login():
    print("----开始登陆----")


login()
# ----开始验证----
# ----开始登陆----
print("*" * 50)


# 外层函数不用函数名参数也能运行,但是不能使用装饰器了
def function_out():
    def function_in(func, a):
        print("----开始验证----")

        # 调用login并返回
        return func(a)

    return function_in


def login(a):
    print("----开始登陆----")
    return a + 10


res = function_out()
print(res(login, 1))
