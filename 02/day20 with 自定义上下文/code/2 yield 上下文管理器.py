'''
思路:
    def myopen(file_name, mode, encoding):
        上文(打开资源)
        yield
        下文(关闭资源)


    装饰器装饰函数的步骤:
        1.导入模块
            from contextlib import contextmanager
        2.开始装饰



yield可以返回值,并暂停函数

yield 的作用就是把一个函数变成一个 generator，带有 yield 的函数不再是一个普通函数，
Python 解释器会将其视为一个 generator，调用 fab(5) 不会执行 fab 函数，而是返回一个 iterable 对象！
在 for 循环执行时，每次循环都会执行 fab 函数内部的代码，执行到 yield b 时，fab 函数就返回一个迭代值，
下次迭代时，代码从 yield b 的下一条语句继续执行，而函数的本地变量看起来和上次中断执行前是完全一样的，于
是函数继续执行，直到再次遇到 yield。
'''
import os
import sys
os.chdir(sys.path[0])


from contextlib import contextmanager


# 用它装饰,让函数有 __enter__ 和 __exit__ 方法
@ contextmanager
def myopen(file_name, mode='r', encoding='utf-8'):
    print("进入上文")
    # 1.打开文件
    file = open(file_name, mode, encoding=encoding)

    # 2.返回资源
    yield file      # 返回数据,暂停函数执行


    # 下文
    # 3.关闭资源
    print("进入下文")
    file.close()


with myopen('hello.txt', mode='r', encoding='utf-8') as file:
    data = file.read()
    print(data)

# 进入上文
# nihao,zaima
# buhao,zaijian
# 进入下文