"""globals() 函数会以字典类型返回当前位置的全部全局变量。
"""

a = 1
b = 2
c = a + b

print(globals())
# {'__name__': '__main__', '__doc__': None, '__package__': None,
#   '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000001D0E7181AD0>,
#   '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>,
#   '__file__': 'd:\\Python\\PythonLearn\\01\\常用函数\\globals.py', '__cached__': None,
#   'a': 1, 'b': 2, 'c': 3
# }
