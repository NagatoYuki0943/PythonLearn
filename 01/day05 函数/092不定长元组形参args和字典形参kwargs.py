'''
在形参前面加上一个*,该形参变为不定长形参,可以接受所有的位置实参,类型是元组         没有参数名字
在形参前边加上两个**.改形参变为不定长字典形参,可以接受所有的关键字实参,类型是字典   有参数名字
'''


def func(*args, **kwargs):
    print(args)
    print(kwargs)
    print("*" * 50)


func(1, 4, 6, 2, 65, 3)
# (1, 4, 6, 2, 65, 3)
# {}


func(a=1, b=2, c=3)
# ()
# {'a': 1, 'b': 2, 'c': 3}


func(4, 'a', a=1, b=2, c=3)


# (4, 'a')
# {'a': 1, 'b': 2, 'c': 3}


# 简单应用 求和功能


def add(*args, **kwargs):
    sum = 0
    for i in args:
        sum += i

    # 遍历dict的values
    for i in kwargs.values():
        sum += i

    return sum


res = add(1, 2, 3, 4, a=5, b=6, c=7)
print(res)  # 28