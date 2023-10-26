'''
try:
    可能发生异常的代码
excerpt 异常的类型:
    发生异常执行的代码
'''

print("其他的代码")
num = input("请输入一个数字:")

try:
    res = 10 / int(num)
    print("计算得到的结果是:" + str(res))
except ZeroDivisionError:
    """只能捕获单个异常,捕获不为0时的异常"""
    print("傻逼啊你,除0???")

print("其他的代码")

