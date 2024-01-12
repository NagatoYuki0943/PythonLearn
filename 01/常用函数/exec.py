"""
execfile() 函数可以用来执行命令。

语法
    execfile(str[, globals[, locals]])

参数
    str      -- 运行的命令。
    globals  -- 变量作用域，全局命名空间，如果被提供，则必须是一个字典对象。
    locals   -- 变量作用域，局部命名空间，如果被提供，可以是任何映射对象。
"""

exec("print('Hello, world!')")
# Hello, world!

with open("locals.py", encoding="utf-8") as f:
    exec(f.read())
# {'__name__': '__main__', '__doc__': 'locals() 函数会以字典类型返回当前位置的全部局部变量_summary_\n', '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x0000028889791B90>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'c:\\Users\\Administrator\\Desktop\\self\\PythonLearn\\01\\常用函数\\exec.py', '__cached__': None, 'f': <_io.TextIOWrapper name='locals.py' mode='r' encoding='utf-8'>, 'x': 10}
# {'x': 1, 'y': 2}
# {'x': 1, 'y': 2, 'z': 3}
