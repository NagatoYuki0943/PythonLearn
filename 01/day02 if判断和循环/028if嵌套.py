"""
if 判断条件1:
    判断条件1 成立,会执行的代码
    if 判断条件2:
        判断条件1成立, 判断条件2成立执行的代码
    else:
        判断条件1成立, 判断条件2不成立执行的代码
else:
    判断条件1不成立,会执行的代码

"""

money = int(input("请输入你的硬币数:"))

if money >= 2:
    seat = eval(input("车上的空位数:"))
    if seat > 2:
        print("坐下吧")
    else:
        print("站着")
else:
    print("走路吧")
