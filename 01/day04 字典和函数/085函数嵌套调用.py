'''
在一个函数中调用另一个函数
'''

def calc(a, b):
    s1 = add(a, b)
    s2 = subtract(a, b)
    return s1, s2


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


res = calc(5, 10)
print(res[0])   # 15
print(res[1])   # -5