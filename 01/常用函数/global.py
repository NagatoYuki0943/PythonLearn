"""global 关键字"""

sum = 0


def print_sum():
    # 当只使用全局变量时,python可以自动去全局变量中找变量
    print(sum)


def add(x, y):
    # 当要修改全局变量时，需要使用global关键字引入更改的变量
    global sum
    sum = x + y
    print(sum)


print_sum()  # 0
add(2, 3)  # 5


# 不过要主要下面全局变量是可变类型,在函数中修改全局变量是可以的,但是不能使用 = 赋值,否则就变为局部变量

d = []


def f():
    d.append(1)


f()
print(d)  # [1]

d = {}


def f():
    d[1] = "a"


f()
print(d)  # {1: 'a'}
