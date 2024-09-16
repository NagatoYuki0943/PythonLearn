"""
issubclass() 方法用于判断参数 class 是否是类型参数 classinfo 的子类。

语法
    issubclass(class, classinfo)
参数
    class     -- 类。
    classinfo -- 类。
"""


class A: ...


class B: ...


class C(A, B): ...


class D(A): ...


print(issubclass(C, A))  # True
print(issubclass(C, B))  # True
print(issubclass(D, A))  # True
print(issubclass(D, B))  # False
