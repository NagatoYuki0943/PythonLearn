'''
主函数有返回值的情况下
要在内层函数返回

def function_in(参数):
    return func(参数)

'''


def function_out(func):

    def function_in(*args, **kwargs):
        print("----开始验证----")

        # 调用login并返回
        return func(*args, **kwargs)

    return function_in


@ function_out
def login(*args, **kwargs):
    print('----开始登陆----')
    print("args: ", args)
    print("kwargs: ", kwargs)
    return args[0] + 10


res = login(4, 5, id=10)
print(res)
# ----开始验证----
# ----开始登陆----
# args:  (4, 5)
# kwargs:  {'id': 10}
# 14

