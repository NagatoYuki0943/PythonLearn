try:
    # 尝试执行的代码
    result = 10 / 1
except ZeroDivisionError:
    # 如果发生ZeroDivisionError异常，执行这里的代码
    print("除数不能为零")
else:
    # 如果没有异常发生，执行这里的代码
    print("除法运算成功")
finally:
    # 无论是否发生异常，都会执行这里的代码
    print("这是清理代码，总是会执行")

# 除法运算成功
# 这是清理代码，总是会执行

print()

try:
    # 尝试执行的代码
    result = 10 / 0
except ZeroDivisionError:
    # 如果发生ZeroDivisionError异常，执行这里的代码
    print("除数不能为零")
else:
    # 如果没有异常发生，执行这里的代码
    print("除法运算成功")
finally:
    # 无论是否发生异常，都会执行这里的代码
    print("这是清理代码，总是会执行")

# 除数不能为零
# 这是清理代码，总是会执行
