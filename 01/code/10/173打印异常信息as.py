'''

try:
    可能发生异常的代码
excerpt 异常的类型 as 变量:
    print(变量)


'''


# 写法1
print("其他的代码")
num = input("请输入一个数字:")

try:
    res = 10 / int(num)
    print("计算得到的结果是:" + str(res))

except (ZeroDivisionError,ValueError) as error:
    print(error)
    # division by zero
    # invalid literal for int() with base 10: 'a'
