'''
闭包构成的条件：
* 存在函数的嵌套关系
* 内层函数引用了外层函数的临时变量
* 外层函数返回内层函数的引用（地址）
'''

def function_out(number):
    print('1 ---- function_out ----num:', number)

    def function_in(number_in):
        print('2 ---- function_in -----num:', number)
        print('3 ---- function_in -----num_in:', number_in)

    return function_in


# 赋值给变量再调用
function_in = function_out(0)
# 1 ---- function_out ----num: 0

# 可以看出闭包可以防止外部函数的变量被释放
function_in(1)
# 2 ---- function_in -----num: 0   
# 3 ---- function_in -----num_in: 1

# 直接调用
function_out(2)(3)
# 1 ---- function_out ----num: 2   
# 2 ---- function_in -----num: 2   
# 3 ---- function_in -----num_in: 3