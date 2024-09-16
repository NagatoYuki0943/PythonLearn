# 初始化方式有2种
a = []
b = [None] * 10


print(a)  # []
print(b)  # [None, None, None, None, None, None, None, None, None, None]

for i in range(10):
    a.append(i)
    b[i] = i

print(a)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(b)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
