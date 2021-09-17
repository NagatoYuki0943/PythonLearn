'''
全局变量： 就是在函数外部定义的变量。
在函数内部可以访问全局变量的值，
不止直接修改全局变量, 如果想要修改全局变量的值，需要使用 global 关键字引用 php要使用 global 引入才能访问和修改,不使用global声明的变量是一个新的局部变量
C语言直接使用或修改即可,不用使用global引用
'''
num = 100

def func():
    # 使用global引入全局变量,直接定义的话是一个局部变量,要在使用之前引用,不然报错
    global num
    print(num)      # 可以直接使用
    # 要修改就要使用 global 引入
    num = 200
    print(num)      # 200

func()


age = 15


def func1():
    # 这样赋值是相当于新建了一个局部变量,不影响全局变量
    age = 16


def func2():
    print(age)


func1()
func2() # 15