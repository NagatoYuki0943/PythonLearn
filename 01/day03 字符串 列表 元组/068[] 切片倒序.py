xs = [1, 2, 3, 4, 5]

## 正序
for x in xs:
    print(x, end=" ")
print()
# 1 2 3 4 5

for x in xs[0:4]:
    print(x, end=" ")
print()
# 1 2 3 4

for x in xs[0::2]:
    print(x, end=" ")
print()
# 1 3 5

for x in xs[0:4:2]:
    print(x, end=" ")
print()
# 1 3

print("*" * 20)

## 倒序,开始结束id也要从右往左数
for x in xs[::-1]:
    print(x, end=" ")
print()
# 5 4 3 2 1

# 从-2开始,忽略最后1个
for x in xs[-2::-1]:
    print(x, end=" ")
print()
# 4 3 2 1

# 从-2开始,忽略最后1个
# 0含义是到1就结束
for x in xs[-2:0:-1]:
    print(x, end=" ")
print()
# 4 3 2
