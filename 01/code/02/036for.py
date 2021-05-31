'''
for循环/遍历
for 变量 in 字符串:
    代码
for 循环也称为 for 遍历,会将字符串中的字符全部取到
'''

# 一次打印一个字符
for i in 'hello':
    print(i, end=" ")  # h e l l o
print()


# range(n) 生成  [0,n) 序列
for i in range(5):
    print(i, end=" ")  # 0 1 2 3 4
print()


# range(m,n) 生成 [m,n) 序列
for i in range(1, 5):
    print(i, end=" ")  # 1 2 3 4
print()


# range(m,n,step) 生成 [m,n) 序列,步长为 step
for i in range(1, 6, 2):
    print(i, end=" ")  # 1 3 5
print("============================")

# for嵌套
for i in range(1, 5):
    for j in range(1, 5):
        print(j * i, end=" ")
print()