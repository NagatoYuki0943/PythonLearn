"""locals() 函数会以字典类型返回当前位置的全部局部变量。"""

x = 10

print(locals())
# {'__name__': '__main__', '__doc__': 'locals() 函数会以字典类型返回当前位置的全部局部变量。\n',
# '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x0000028DC5BD1B90>,
# '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>,
# '__file__': 'c:\\Users\\Administrator\\Desktop\\self\\PythonLearn\\01\\常用函数\\locals.py', '__cached__': None, 'x': 10}


def func(x, y):
    print(locals())  # {'x': 1, 'y': 2}
    z = x + y
    print(locals())  # {'x': 1, 'y': 2, 'z': 3}
    return z


func(1, 2)
