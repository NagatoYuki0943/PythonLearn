'''
列表嵌套
里面如果是字符串也能接着遍历,数字就不行了

'''
list1 = [
    ['Tom', 'male', 15],
    ['Jerry', 'female', 18],
    ['Duck', 'futa', 18]
]

for i in list1:
    for j in i:
        print(j, end='\t')
    print()

# Tom	male	15
# Jerry	female	18
# Duck	futa	18
print('-' * 50)

print(list1[1])         # ['Jerry', 'female', 18]
print(list1[1][1])      # female
print(list1[1][1][1])   # e
