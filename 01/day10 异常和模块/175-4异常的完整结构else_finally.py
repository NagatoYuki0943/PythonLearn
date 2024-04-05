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

def func() -> int:
    try:
        raise ValueError("Bad Value")
    except ValueError:
        raise Exception("We not expect this")
        # 这里不管用,还是强制执行finally
        return 1
    finally:
        # 正常运行就返回0
        return 0


print(func())
# 0