'''
一次读取一行内容
文件对象.readline()

一次读取所有行,返回值是列表,每一项都是一行内容
文件对象.readlines()

'''

f = open('文件/1.txt', 'r', encoding='utf-8')

res = f.readline()  # 111
print(res)
res = f.readline()  # 222
print(res)


# 一次读取所有行,返回值是列表,每一项都是一行内容
res = f.readlines()
print(res)           # ['333\n', '444\n', '555']

# 去除换行符
res = [i.strip() for i in res]

print(res)          # ['333', '444', '555']


f.close()



