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
    # 即使退出也会执行finally
    exit()
finally:
    print("finally is being executed")
# finally is being executed
