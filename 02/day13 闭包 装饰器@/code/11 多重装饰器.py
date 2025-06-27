"""
应用顺序(函数定义时):从内到外，靠近函数的装饰器先应用。
执行顺序(函数调用时):从外到内，最外层的装饰器先执行。
"""


def decorator_a(func):
    print("decorator_a")

    def wrapper():
        print("wrapper_a")
        return func()

    return wrapper


def decorator_b(func):
    print("decorator_b")

    def wrapper():
        print("wrapper_b")
        return func()

    return wrapper


@decorator_a
@decorator_b
def my_function():
    print("my_function")


my_function()
# decorator_b
# decorator_a
# wrapper_a
# wrapper_b
# my_function
