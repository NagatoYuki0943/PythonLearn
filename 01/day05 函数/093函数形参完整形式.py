'''
顺序
普通参数,不定长元组参数,默认参数(放在*args前面的话,默认值就没有意义了),不定长字典参数(默认参数也是键值对,要是放在**wkargs后面就永远都是默认值了)
a, *args, b=0, **kwargs
'''

# 先普通,再默认参数
def func1(a, b=0):
    pass


# 先普通,再默认参数,再*args,默认参数没法再适用面默认值了
def func2(a, b=0, *args):
    print('a', a)
    print('b', b)
    print(args)
    print('*' * 50)
func2(1,2,3,4)
# a 1
# b 2
# (3, 4)


# 先普通,再*args,再默认参数
def func3(a, *args, b=0):
    print('a', a)
    print('b', b)
    print(args)
    print('*' * 50)

# 这样b使用默认值,其他都给了*args
func3(1, 2, 3)
# a 1
# b 0
# (2, 3)

# 使用关键字传参,可以让b有值
func3(1, 2, b=3)
# a 1
# b 3
# (2,)


# 普通参数,不定长元组参数,默认参数,不定长字典参数(默认参数也是键值对,要是放在**wkargs后面就永远都是默认值了)
def func4(a, *args, b=0, **kwargs):
    print('a', a)
    print('b', b)
    print(args)
    print(kwargs)
    print('*' * 50)


func4(1,2,b=4,c=5)
# a 1
# b 4
# (2,)
# {'c': 5}

