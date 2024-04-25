import inspect

def var_dict(*args):
    """
    将变量转化为字典形式, key是变量的字符串名称, value是变量的值
    https://github.com/NagatoYuki0943/transformers-benchmarks/blob/main/micro_bench.ipynb

    ::example
        a = torch.randn(n, n)
        b = torch.randn(n, n)
        result = var_dict(a, b)
        result = {
            "a": a,
            "b": b,
        }
    """
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    print(callers_local_vars)
    # {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x0000019197011A90>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'd:\\Python\\PythonLearn\\01\\获取变量名称\\获取变量名称.py', '__cached__': None, 'inspect': <module 'inspect' from 'F:\\Miniconda3\\envs\\pytorch\\Lib\\inspect.py'>, 'var_dict': <function var_dict at 0x000001919702DBC0>, 'a': 3, 'b': 4, 'c': 5}串.py'), ('__cached__', None), ('inspect', <module 'inspect' from 'F:\\Miniconda3\\envs\\pytorch\\Lib\\inspect.py'>), ('var_dict', <function var_dict at 0x000002A1DA19D8A0>), ('a', 3), ('b', 4), ('c', 5)])

    # return dict([(name, val) for name, val in callers_local_vars if val is arg][0]
    #             for arg in args)

    # 这是上面一行的简写
    var_dict = {}
    # 遍历传入参数的值
    for arg in args:
        # 遍历全部参数的 name 和 value
        for name, value in callers_local_vars:
            # 如果 全部参数的值为传入参数的值,就保存
            if value is arg:
                var_dict[name] = value
    print(var_dict)
    # {'a': 3, 'b': 4, 'c': 5}
    return var_dict


if __name__ == "__main__":
    a = 3
    b = 4
    c = 5
    var_dict(a, b, c)

