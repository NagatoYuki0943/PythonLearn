"""
写法1:
try:
    可能发生异常的代码
excerpt:
    发生异常执行的代码

    缺点:不能获取异常的描述信息

写法2:
try:
    可能发生异常的代码
excerpt Exception as e:
    发生异常执行的代码
    print(e)

Exception是常见异常类的父类
"""

print("其他的代码")
num = input("请输入一个数字:")

try:
    res = 10 / int(num)
    print("计算得到的结果是:" + str(res))

except Exception as error:
    print(error)
    # division by zero
    # invalid literal for int() with base 10: 'a'
