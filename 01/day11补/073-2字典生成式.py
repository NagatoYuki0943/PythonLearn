d1 = {'a': 4, 'b': 2, 'c': 1, 'd': 5, 'e': 6, 'f': 0, 'g': -8}

d2 = {k: v for k, v in d1.items() if v > 0}
print(d2)
# {'a': 4, 'b': 2, 'c': 1, 'd': 5, 'e': 6}


# 交换 k 和 v
# 方法1
print({v: k for k, v in d1.items()})
# {4: 'a', 2: 'b', 1: 'c', 5: 'd', 6: 'e', 0: 'f', -8: 'g'}


# 方法2  使用zip压缩更高效
print(dict(zip(d1.values(), d1.keys())))
# {4: 'a', 2: 'b', 1: 'c', 5: 'd', 6: 'e', 0: 'f', -8: 'g'}
