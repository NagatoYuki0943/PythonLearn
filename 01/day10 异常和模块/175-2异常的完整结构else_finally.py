'''
try:
    # 尝试执行的代码
except Exception as e:
    # 发生异常执行这里的代码
else:
    # 如果没有异常发生，执行这里的代码
finally:
    # 无论是否发生异常，都会执行这里的代码
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
