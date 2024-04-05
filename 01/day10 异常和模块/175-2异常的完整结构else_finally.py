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
    print("Handing ValueError")
finally:
    print("finally is being executed")

# Handing ValueError
# finally is being executed


try:
    raise ValueError("Bad Value")
except ValueError:
    raise Exception("We not expect this")
finally:
    # 捕获异常后也会执行这个
    print("finally is being executed")
# finally is being executed

