"""
* ** 拆包,将元组和字典拆开

传递的是 (10, 20, 30) {'a': 10, 'b': 20} 识别成两个复杂元素
func01(args, kwargs)


这样可以拆包,拆成 10, 20 ,30, a=10, b=20, 这样就能被下一个函数的可变参数识别了
func01(*args, **kwargs)

"""


#
def func01(*args, **kwargs):
    print("---------- func01 ----------")
    print("args:\t", args)
    print("kwargs:\t", kwargs)


def func02(*args, **kwargs):
    print("---------- func02 ----------")
    print("args:\t", args)
    print("kwargs:\t", kwargs)

    # * ** 拆包,将元组和字典拆开
    print("*args:\t", *args)
    # print(**kwargs)

    # 此处没有拆包,导致参数传递过去不符合要求
    # 传递的是 (10, 20, 30) {'a': 10, 'b': 20} 识别成两个复杂元素
    func01(args, kwargs)

    # 这样可以拆包,拆成 10, 20 ,30, a=10, b=20, 这样就能被下一个函数的可变参数识别了
    func01(*args, **kwargs)


if __name__ == "__main__":
    func02(10, 20, 30, a=10, b=20)

    # ---------- func02 ----------
    # args:    (10, 20, 30)
    # kwargs:  {'a': 10, 'b': 20}
    # *args:   10 20 30

    # func01(args, kwargs)
    # ---------- func01 ----------
    # args:    ((10, 20, 30), {'a': 10, 'b': 20})
    # kwargs:  {}

    # func01(*args, **kwargs)
    # ---------- func01 ----------
    # args:    (10, 20, 30)
    # kwargs:  {'a': 10, 'b': 20}
