"""
主函数有返回值的情况下
要在内层函数返回

def function_in(参数):
    return func(参数)

"""


def function_out(func):
    def function_in(id):
        print("----开始验证----")

        # 调用login并返回
        return func(id)

    return function_in


@function_out
def login(id):
    print("----开始登陆----")
    return id + 10


res = login(5)
print(res)
# ----开始验证----
# ----开始登陆----
# 15
