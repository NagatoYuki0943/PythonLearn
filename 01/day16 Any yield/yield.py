'''
斐波那契（Fibonacci）數列是一个非常简单的递归数列，除第一个和第二个数外，任意一个数都可由前两个数相加得到。
用计算机程序输出斐波那契數列的前 N 个数是一个非常简单的问题

yield可以返回值,并暂停函数

yield 的作用就是把一个函数变成一个 generator，带有 yield 的函数不再是一个普通函数，
Python 解释器会将其视为一个 generator，调用 fab(5) 不会执行 fab 函数，而是返回一个 iterable 对象！
在 for 循环执行时，每次循环都会执行 fab 函数内部的代码，执行到 yield b 时，fab 函数就返回一个迭代值，
下次迭代时，代码从 yield b 的下一条语句继续执行，而函数的本地变量看起来和上次中断执行前是完全一样的，于
是函数继续执行，直到再次遇到 yield。
'''

def fab(max): 
    n, a, b = 0, 0, 1 
    while n < max: 
        yield b      # 使用 yield
        # print b 
        a, b = b, a + b 
        
        n += 1
 

for n in fab(5): 
    print(n)
# 1
# 1
# 2
# 3
# 5


f = fab(5) 
# 迭代器的形式
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
# 1
# 1
# 2
# 3
# 5