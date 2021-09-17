
n = int(input('请输入正方形的长度:'))


j = 0
while j < n:
    i = 0
    while i < n:
        print('*', end=' ')
        i += 1
    print()
    j += 1


for i in range(n):
    for j in range(n):
        print("*",end="")   # ******
    print()