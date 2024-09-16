"""
匿名函数作为函数的参数使用

"""


def calc(num1, num2, func):
    """
    四则运算
    :param num1:    数字2
    :param num2:    数字1
    :param func:    函数,要进行的云散
    :return:        运算结果
    """
    return func(num1, num2)


print(calc(2, 3, lambda x, y: x + y))  # 5
print(calc(2, 3, lambda x, y: x - y))  # -1
print(calc(2, 3, lambda x, y: x * y))  # 6
print(calc(2, 3, lambda x, y: x / y))  # 0.6666666666666666
print(calc(2, 3, lambda x, y: (x / y) * 10))  # 6.666666666666666
