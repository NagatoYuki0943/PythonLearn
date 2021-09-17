'''
写法1:
try:
    可能发生异常的代码
excerpt (异常的类型1,异常的类型2...):
    发生异常执行的代码


写法2
try:
    可能发生异常的代码

excerpt 异常的类型1:
    发生异常1执行的代码

excerpt 异常的类型2:
    发生异常2执行的代码
...

'''

# 写法1
print("其他的代码")
num = input("请输入一个数字:")

try:
    res = 10 / int(num)
    print("计算得到的结果是:" + str(res))

except (ZeroDivisionError,ValueError):
    """多个异常"""
    print("傻逼啊你,除0或者输入的不是数字???")



print("==================")


# 写法2
num = input("请输入一个数字:")

try:
    res = 10 / int(num)
    print("计算得到的结果是:" + str(res))

except ZeroDivisionError:
    print("傻逼啊你,除0???")

except ValueError:
    print("傻逼啊你,不输入正确的数字???")

