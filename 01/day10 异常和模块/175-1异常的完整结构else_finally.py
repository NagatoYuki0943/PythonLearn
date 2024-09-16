"""
try:
    # 尝试执行的代码
except Exception as e:
    # 发生异常执行这里的代码
else:
    # 如果没有异常发生，执行这里的代码
finally:
    # 无论是否发生异常，都会执行这里的代码
"""

while True:
    num = input("请输入一个数字:")

    try:
        res = 10 / int(num)
        print("result =", res)

    except Exception as error:
        print(error)

    else:
        print("没有发生异常else中会执行")

    finally:
        print("不管有没有异常finally中都会执行")
