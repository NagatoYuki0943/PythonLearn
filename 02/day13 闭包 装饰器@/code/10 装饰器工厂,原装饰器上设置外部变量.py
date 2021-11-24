'''
三层函数
@ test(0)  # 这是传递给test函数的变量,没有参数也要有括号
 过程解释
 @test(0) 分解为2步
 第一步:
    1) 执行 test(0)  -->  返回 func_out 引用
    2) @ 第一步的结果  -->  @func_out
 下一步：
    1) login = func_out(login)

'''


def test(choice):
    '''
    返回装饰器的引用,装饰器工厂,可以根据参数返回不同的装饰器
    '''
    print(choice)

    if choice == 0:
        # 装饰器
        def func_out(func):
            def func_in():
                print("----开始验证----")
                func()
            return func_in
        return func_out

    elif choice == 1:
        # 装饰器
        def func_out(func):
            def func_in():
                print("----开始注册----")
                func()
            return func_in
        return func_out


@ test(0)  # 这是传递给test函数的变量,没有参数也要有括号
# 过程解释
# @test(0) 分解为2步
# 第一步:
# 1) 执行test("0)   -->  返回 func_out 引用
# 2) @ 第一步的结果  -->  @func_out
# 下一步：
# login = func_out(login)
def login():
    print("----开始登陆----")
login()
# login.py
# ----开始验证----
# ----开始登陆----


@ test(1)
def register():
    print("----开始登陆----")
register()
# 1
# ----开始注册----
# ----开始登陆----