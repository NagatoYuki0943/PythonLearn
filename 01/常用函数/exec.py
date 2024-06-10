"""
exec() 函数可以用来执行代码

语法
    execfile(str[, globals[, locals]])

参数
    str      -- 运行的命令。
    globals  -- 变量作用域，全局命名空间，如果被提供，则必须是一个字典对象。
    locals   -- 变量作用域，局部命名空间，如果被提供，可以是任何映射对象。

**注意 exec 可以用来修改全局变量，但是不能修改局部变量**
具体来说 exec 运行的代码是在另一个frame中运行的，和当前的frame无关，因此2个同名的局部变量是互不影响的，而全局变量是会影响的
"""


a = 0
exec("a = 1")
print(a)
# 1


def f():
    a = 0
    exec("a = 1")
    print(a)
f()
# 0

print()


def f():
    a = 0
    print(locals())
    exec("print(locals());a = 1;print(locals())")
    print(locals())
    print(a)
f()
# {'a': 0}
# {'a': 0}
# {'a': 1} # exec 中确实改变了局部变量
# {'a': 0} # 但是从 exec 出来后却没有改变
# 0

print()


# 官方建议如下,自己建立一个字典传递给 locals 变量, 返回的是修改的局部变量，exec 没法修改局部变量

def f():
    a = 0
    result = {}
    exec("a = 1", globals(), result)
    print(result)
    print(a)
f()
# {'a': 1}
# 0
