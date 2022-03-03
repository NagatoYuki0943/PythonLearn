'''
zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
列表可以转换成zip再转换回来
字典可以转换成zip再转换回来

zip(item1, item2...)

'''
l1 = [1, 2, 'a', True]


z1 = zip(l1)
print(z1)  # <zip object at 0x0000013A7868FE88>
print(list(z1))     # [(1,), (2,), ('a',), (True,)]


d1 = {'a': 1, 'b': 2, 'c': 3}
z2 = zip(d1.items())
print(list(z2))     # [(('a', 1),), (('b', 2),), (('c', 3),)]


z3 = zip(d1.keys(), d1.values())
print(dict(z3))     # {'a': 1, 'b': 2, 'c': 3}


# 快速交换key和value
d4 = zip(d1.values(), d1.keys())
print(dict(d4))     # {1: 'a', 2: 'b', 3: 'c'}


z4 = zip([[1, "a"], [2, "b"], [3, "c"]])
print(tuple(z4))    # (([1, 'a'],), ([2, 'b'],), ([3, 'c'],))


# zip * 将数据分为两组
z5 = zip(*[[1, "a"], [2, "b"], [3, "c"]])
print(*[[1, "a"], [2, "b"], [3, "c"]])  # [1, 'a'] [2, 'b'] [3, 'c']
print(tuple(z5))    # ((1, 2, 3), ('a', 'b', 'c'))