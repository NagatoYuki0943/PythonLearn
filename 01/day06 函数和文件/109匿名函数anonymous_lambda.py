"""
使用 lambda 关键字定义的函数就是匿名函数

变量名 = lambda [参数列表]：表达式
匿名函数自调用
(lambda [参数列表]：表达式)()

1.匿名函数中不能使用if语句,while语句,for循环,只能编写单行的表达式,或函数调用,普通函数都可以
2.匿名函数中返回结果不用return,表达式的运行结果就是返回结果
3.匿名函数也可以不返回结果,如: lambda : print('hello world')

"""


# 1.无参无返回值
def func1():
    print("普通函数,无参,无返回值")


lambda1 = lambda: print("匿名函数,无参,无返回值")
# 函数自调用
(lambda: print("匿名函数,无参,无返回值"))()

func1()  # 普通函数,无参,无返回值
lambda1()  # 匿名函数,无参,无返回值
print("*" * 50)


# 2.有参,无返回值
def func2(name):
    print("普通函数,有参,无返回值", name)


lambda2 = lambda name: print("匿名函数,有参,无返回值", name)
func2("Tom")  # 普通函数,有参,无返回值 Tom
lambda2("Jelly")  # 匿名函数,有参,无返回值 Jelly
print("*" * 50)


# 3.无参,有返回值
def func3():
    return "普通函数,无参,有返回值"


lambda3 = lambda: "普通函数,无参,有返回值"
print(func3())  # 普通函数,无参,有返回值
print(lambda3())  # 普通函数,无参,有返回值
print("*" * 50)


# 4.有参,有返回值
def func4(*args):
    return args[0] + args[1]


lambda4 = lambda *args: args[0] + args[1]

print(func4(1, 3))  # 4
print(lambda4(1, 3))  # 4
