"""
函数的文档说明:
    函数注释,告诉别人函数的作用
    位置在函数名下面
"""


def func():
    """
    打印输入Hello
    :return:
    """
    print("Hello")


func()
# 查看函数的文档注释,可以使用help(函数名)  函数名没有括号
# 或者按住ctrl + 点击,里面是pass,因为是使用C语言实现的
help(print)
help(func)
# func()
#     打印输入Hello
#     :return:
