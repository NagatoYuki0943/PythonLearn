
def function(chioce):
    if chioce == 0:

        def func_out(func):
            def func_in(*args, **kwargs):
                print('000000')
                return func(*args, **kwargs)
            return func_in
        return func_out

    elif chioce == 1:
        
        def func_out(func):
            def func_in(*args, **kwargs):
                print(111111)
                return func(*args, **kwargs)
            return func_in
        return func_out

@ function(0)
@ function(1)
def add(*args, **kwargs):
    return args[0] + args[1]


print(add(1, 2))
