'''
可以使用 for 和 while 遍历
'''

list1 = [1, 2, 3, 'a', True]

for i in list1:
    print(i, end=' ')           # 1 2 3 a True
print()

j = 0
while j < len(list1):
    print(list1[j], end=" ")    # 1 2 3 a True
    j += 1
