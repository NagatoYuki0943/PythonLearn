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


try:
    raise ValueError("Bad Value")
except ValueError:
    # 即使退出也会执行finally
    exit()
finally:
    print("finally is being executed")
# finally is being executed

