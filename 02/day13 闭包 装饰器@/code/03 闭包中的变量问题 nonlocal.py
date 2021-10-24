'''
如果在内层强制使用外层变量,使用nonlocal修饰变量
不使用函数内层变量,而是使用外层函数变量
nonlocal number 
'''


def function_out(number):

    def function_in():
        # 在内层定义了和外层同名的变量,无论在上面和下面,都会使用内部的,放在下部的会报错,因为找不到
        # 如果在内层强制使用外层变量,使用nonlocal修饰变量
        nonlocal number
        
        # number = 88
        print("function_in num=", number)
        number = 88     # 默认下面会报错,因为上面找不到

    return function_in



# 可以看出闭包可以防止外部函数的变量被释放
function_out(10)()
# function_in num= 88
