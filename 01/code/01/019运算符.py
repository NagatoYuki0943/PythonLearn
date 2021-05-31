'''
算术运算符
    + - * /
    // 整除(求商)
    % 取余数
    ** 指数,幂运算
    () 可以改变优先级

赋值运算符
    = 将等号右边的结果赋值给等号左边的变量
    等号左边,必须是变量,不能是具体的数字

复合赋值运算符
    +=  c+=a  => c = c + a

    Python没有 ++ --

比较运算符
    == 判断是否相等, 相等是 True. 不相等是 False
    != 判断是否不相等, 不相等是 True, 相等 False
    >
    <
    >=
    <=

逻辑运算符
    and 优先级高于 or

    and  逻辑与, 连接的两个条件都必须为 True,结果为 True,  一假为假
        如果第一个条件为 False,就不会再判断第二个条件
    or   逻辑或, 连接的两个条件都为 False,结果为 False,    一真为真
        如果第一个条件为 True,第二个条件就不会再判断了
    not  逻辑非, 取反,原来是 True,变为 False,原来是 False,变为 True
'''
num1 = 15
num2 = 7
print(num1 / num2)  # 2.142857142857143
print(num1 // num2)  # 2
print(2 ** 3)  # 8

# and or not
# &&  || !
flag1 = True
flag2 = False
print(flag1 and flag2)  # False
print(flag1 or flag2)  # True

# not 取反 !
print(not flag1)  # False


