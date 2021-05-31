'''
程序代码为什么会报错?
因为不符合语法, 因为 python 的作者在代码中使用了 if 判断,如果除数为 0 ,就会在代码中抛出异常错误,
抛出异常:
    raise 异常对象  # 当程序代码遇到 raise 的时候,程序就报错了


异常对象 = 异常类(参数)

抛出自定义异常:
    1. 自定义异常类,继承 Exception 或者 BaseException
    2. 选择书写,定义 __init__方法,定义__str__ 方法
    3. 在合适的时机抛出异常对象即可

'''

# 定义异常类 密码长度不足
class PasswordLengthError(Exception):
    pass
    # def __str__(self):
    #     return "xxx"


# 等同于系统提供定义函数
def get_password():
    password = input("请输入密码:")
    if(len(password)) >= 6:
        print("密码长度合格")
    else:
        # 抛出异常 抛出自定义异常对象
        raise PasswordLengthError("密码长度不足6位")
        # PasswordLengthError: 密码长度不足6位

get_password()