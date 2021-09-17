'''
try:
    可能发生异常的代码
excerpt Exception as e:
    发生异常执行的代码
    print(e)

else:
    代码没有发生异常才执行

finally:
    不管有没有发生异常都会执行

'''

print("其他的代码")
num = input("请输入一个数字:")

try:
    res = 10 / int(num)
    print("计算得到的结果是:" + str(res))

except Exception as error:
    print(error)

else:
    print("没有发生异常else中会执行")

finally:
    print("不管有没有异常finally中都会执行")


print("外部不受影响,都会执行")