'''
`collections.defaultdict(default_factory)`为字典的没有的key提供一个默认的值。
参数应该是一个函数，当没有参数调用时返回默认值。如果没有传递任何内容，则默认为None。

就是取字典的key不存在时不会报错
defaultdict(存放的数据类型)
'''

from collections import defaultdict


# 也可以写成dict = {}
dic = dict()
dic['a'] = 1
dic['b'] = 2

print(dic['a'])     # 1
print(dic['b'])     # 2

# 如果dict中没有对应的key则会抛出KeyError异常。
try:
    print(dic['c'])
except:
    print("no c")   # no c
print("-" * 10)

# 使用defaultdict可以规避这个问题
dic = defaultdict(int)
dic['a'] = 1
dic['b'] = 2

print(dic['a'])     # 1
print(dic['b'])     # 2
print(dic['c'])     # 0  打印默认值
print("-" * 10)


## 常规用法
# defaultdict接受一个类型对象或函数对象，在取值时，如果不存在对应的key则返回对应的函数返回值或默认构造函数的实例对象：
dic_1 = defaultdict(int)
dic_2 = defaultdict(tuple)
dic_3 = defaultdict(list)
dic_4 = defaultdict(str)
dic_5 = defaultdict(set)

print(dic_1['a'])   # 0
print(dic_2['a'])   # ()
print(dic_3['a'])   # []
print(dic_4['a'])   #
print(dic_5['a'])   # set()
print("-" * 10)


## 自定义默认类型
class Cls:
    def __init__(self, val='hello'):
        self.val = val

    def __str__(self):
        return self.val

def fun(val=121):
    return val

dic_1 = defaultdict(Cls)
dic_2 = defaultdict(fun)
print(dic_1['a'])   # hello
print(dic_2['a'])   # 121
print("-" * 10)


## 当我们多次取不存在的相同key对应的默认值时,会多次调用函数或构造函数吗?
def fun(val=121):
    print('创建了默认值')
    return val

dic = defaultdict(fun)
for i in range(1000):
    dic['a']

print('------')
dic['b']
print("-" * 10)
# 创建了默认值
# ------            可以看到，同一个key只会调用了一次取默认值函数。
# 创建了默认值



## 返回的默认值是同一个对象吗？
dic = defaultdict(Cls)

print(dic['a']== dic['a'])  # True
print(dic['a']== dic['b'])  # False     不是同一个对象
