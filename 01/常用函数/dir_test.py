"""
dir() 函数不带参数时，返回当前范围内的变量、方法和定义的类型列表；带参数时，返回参数的属性、方法列表。
如果参数包含方法__dir__()，该方法将被调用。如果参数不包含__dir__()，该方法将最大限度地收集参数信息。
"""

# 查看列表

funcs = dir([])
func: str
funcs = [func for func in funcs if not func.startswith("__")]
print(funcs)
print()
['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']


# 查看元组
funcs = dir(tuple())
func: str
funcs = [func for func in funcs if not func.startswith("__")]
print(funcs)
print()
['count', 'index']


# 查看字典
funcs = dir({})
func: str
funcs = [func for func in funcs if not func.startswith("__")]
print(funcs)
print()
['clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']


# 查看set
funcs = dir(set())
func: str
funcs = [func for func in funcs if not func.startswith("__")]
print(funcs)
['add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint',
'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
