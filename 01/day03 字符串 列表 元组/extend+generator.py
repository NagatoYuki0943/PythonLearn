# extend[list]
x = [1, 2, 4]
x.extend([x[-1] * 2 for _ in range(3)])
print(x)
# [1, 2, 4, 8, 8, 8]


# extend(generator)
x = [1, 2, 4]
x.extend(x[-1] * 2 for _ in range(3))
print(x)
# [1, 2, 4, 8, 16, 32]
