"""
1.位置传参,按照位置进行自动排序

2.关键字传参,指定实参传递给哪个形参,注意点: 关键字必须是函数的形参名

3.混合使用,先写位置传参,在写关键字传参,参数不能重复
"""


def func(a, b, c):
    print(a + b + c)


# 1.位置传参,按照位置进行自动排序
func(1, 2, 3)  # 6


# 2.关键字传参,指定实参传递给哪个形参,注意点: 关键字必须是函数的形参名
func(b=1, a=6, c=15)  # 22


# 3.混合使用,先写位置传参,在写关键字传参,参数不能重复
func(2, b=2, c=6)  # 10
# func(c=1, 2, 3)    先写关键字就报错
