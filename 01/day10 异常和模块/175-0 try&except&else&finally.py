try:
    # 尝试执行的代码
    result = 10 / 1
except ZeroDivisionError as e:
    # 如果发生ZeroDivisionError异常，执行这里的代码
    print(f"除数不能为零, {e}")
except Exception as e:
    # 如果发生其他异常，执行这里的代码
    print(f"发生了其他异常, {e}")
else:
    # 如果没有异常发生，执行这里的代码
    print("除法运算成功")
finally:
    # 无论是否发生异常，都会执行这里的代码
    print("这是清理代码，总是会执行")

print()

# 装饰器
def try_except_else_finally1(func: callable):
    def decorator(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except ZeroDivisionError as e:
            print(f"除数不能为零, {e}")
        except Exception as e:
            print(f"发生了其他异常, {e}")
        else:
            print("除法运算成功")
            return result
        finally:
            print("这是清理代码，总是会执行")
    return decorator


def try_except_else_finally2():
    def decorator(func: callable):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
            except ZeroDivisionError as e:
                print(f"除数不能为零, {e}")
            except Exception as e:
                print(f"发生了其他异常, {e}")
            else:
                print("除法运算成功")
                return result
            finally:
                print("这是清理代码，总是会执行")
        return wrapper
    return decorator


@try_except_else_finally1
def divide1(a, b):
    return a / b

print(divide1(10, 0))  # 除数不能为零, division by zero
print()
print(divide1(10, 1))  # 除数不能为零, division by zero

print()

@try_except_else_finally2()
def divide2(a, b):
    return a / b

print(divide2(10, 0))  # 除数不能为零, division by zero
print()
print(divide2(10, 1))  # 除数不能为零, division by zero
