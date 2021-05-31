num = int(input('请输入数字:'))

i = 0
while i < num:
    j = 0
    while j <= i:
        print("*", end='')
        j += 1
    print()
    i += 1

print('---------------------')


# i 从0开始到num-1
for i in range(num):
    # j从0开始到i
    for j in range(i + 1):
        print("*", end='')
    print()