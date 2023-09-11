"""
列表相加就是extend
"""
a = []

a += [1]
a += ['a']
a.extend([True])

print(a)    # [1, 'a', True]
