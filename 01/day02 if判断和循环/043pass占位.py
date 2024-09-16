"""
if 判断条件:
    pass  # 占位,空代码 让代码不报错
elif 判断条件:
    pass
else:
    pass

"""

a = 0
if a > 10:
    pass  # 占位,空代码 让代码不报错

for i in range(10):
    pass  # 占位,空代码 让代码不报错


# 求出数字的各个位数
num = 765

# 个位
a = num % 10
print(a)  # 5

# 十位
b = (num // 10) % 10
print(b)  # 6

# 百位
c = num // 100
print(c)  # 7
