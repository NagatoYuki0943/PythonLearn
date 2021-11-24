'''
参数, login使用什么参数,内部函数就使用什么函数,还要传递给内部函数调用的函数
'''



def function_out(func):

    #  这个id是login函数的参数
    def function_in(id, password):
        print("开始验证 id =", id, ',password =', password)

        # 要传递给调用的函数
        func(id, password)

    return function_in



# 登录函数
@ function_out
def login(id, password):
    print("开始登陆 id =", id, ',password =', password)


login(1, 1000)
# 开始验证 id = 1 ,password = 1000
# 开始登陆 id = 1 ,password = 1000
