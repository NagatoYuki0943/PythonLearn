"""
# 主函数
login(1, 1000, password=999)

# 内部函数
function_in(*args, **kwargs):
        func(*args, **kwargs)
"""


def function_out(func):
    #  *args, **kwargs是login函数的参数
    def function_in(*args, **kwargs):
        print("开始验证")
        # 要传递给调用的函数,传递函数也要使用 * **
        func(*args, **kwargs)

    return function_in


# 登录函数
@function_out
def login(*args, **kwargs):
    print("开始登陆")
    print("args: ", args)
    print("kwargs: ", kwargs)


login(1, 1000, password=999)
# 开始验证
# 开始登陆
# args:  (1, 1000)
# kwargs:  {'password': 999}
