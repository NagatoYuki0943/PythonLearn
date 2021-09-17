'''
find

从左边开始查找是否存在某个字符串,找第一个位置
mystr.find(substr,start,end)
substr: 要找的内容
start:  开始查找位置,默认是0
end:    结束查找位置之后的位置,默认是 len()
返回结果是 substr 位置的整数下标,找不到返回 -1
'''
str1 = "hello world itcast and itcastcpp"

# 说明参数2是结束下标的下一个位置
print(str1.find('p', 1, 4))  # -1
print(str1.find('o', 1, 5))  # 4

print(str1.find('itcast'))       # 12
print(str1.find('itcast', 15))   # 23
print('---------------------------')


'''
rfind

从右边开始查找是否存在某个字符串,找第一个位置
mystr.rfind(substr,start,end)
substr: 要找的内容
start:  开始查找位置,默认是0                 也是正数
end:    结束查找位置之后的位置,默认是 len()    也是正数
返回结果是 substr 位置的整数下标,找不到返回 -1
'''
print(str1.rfind('itcast'))     # 23
# rfind参数2和参数3也填写正数
print(str1.rfind('itcast', 1, 25))  # 12
print('---------------------------')


'''
index

从左边开始查找是否存在某个字符串,找第一个位置
mystr.index(substr,start,end)
substr: 要找的内容
start:  开始查找位置,默认是0                 也是正数
end:    结束查找位置之后的位置,默认是 len()    也是正数
返回结果是 substr 位置的整数下标,找不到报错
'''
print(str1.index('itcast'))    # 12
#print(str1.index('p', 1, 4))  # 报错了
print('---------------------------')


'''
rindex

从右边开始查找是否存在某个字符串,找第一个位置
mystr.rindex(substr,start,end)
substr: 要找的内容
start:  开始查找位置,默认是0                 也是正数
end:    结束查找位置之后的位置,默认是 len()    也是正数
返回结果是 substr 位置的整数下标,找不到报错
'''
print(str1.rindex('itcast'))     # 23
#print(str1.rindex('itcast1'))   # 报错了
print('---------------------------')


'''
count()

查找count中字符串的出现次数
mystr.count(substr,start,end)
substr: 要找的内容
start:  开始查找位置,默认是0                 也是正数
end:    结束查找位置之后的位置,默认是 len()    也是正数

'''
print(str1.count('aaaa'))       # 0
print(str1.count('hello'))      # 1
print(str1.count('itcast'))     # 2
print(str1.count('itcast', 20)) # 1