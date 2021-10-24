'''
类装饰器
init函数要接收函数名
    __init__(self, func): 
        self.func = func
call方法里面执行func函数
    __call__():
        self.func()


类装饰器执行步骤
# 执行步骤
# 1) test = Test(login)
# 2) test(login的参数) --> 调用
def login(name):
    pass
'''

# 装饰器类
class Test(object):

    # 传入函数名
    def __init__(self, func):
        print("--func--: ", func)

        # 保存函数
        self.func = func


    def __call__(self, *args, **kwargs):
        print('__call__')

        # 调用函数
        return self.func(args[0])


@ Test
# 执行步骤
# 1) test = Test(login)
# 2) test(login的参数) --> 调用
def login(name):
    print("开始登陆: ", name)
    return name

res = login('Tom')
print(res)
# --func--:  <function login at 0x000002D4EDC72EA0>
# __call__
# 开始登陆:  Tom
# Tom