# extend[list]
x = [1, 2, 4]
x.extend([x[-1] * 2 for _ in range(3)])
print(x)
# [1, 2, 4, 8, 8, 8]

x = [1, 2, 4]
y = [x[-1] * 2 for _ in range(3)]
x.extend(y)
print(type(y))
# <class 'list'>
print(x)
# [1, 2, 4, 8, 8, 8]


# extend(generator)
x = [1, 2, 4]
x.extend(x[-1] * 2 for _ in range(3))
print(x)
# [1, 2, 4, 8, 16, 32]

x = [1, 2, 4]
y = (x[-1] * 2 for _ in range(3))
x.extend(y)
print(type(y))
# <class 'generator'>
print(x)
# [1, 2, 4, 8, 16, 32]
