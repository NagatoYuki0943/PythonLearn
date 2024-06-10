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

print_sum()     # 0
add(2, 3)   # 5

