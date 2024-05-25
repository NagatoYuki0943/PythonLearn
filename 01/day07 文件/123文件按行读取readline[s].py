'''
一次读取一行内容
文件对象.readline()

一次读取所有行,返回值是列表,每一项都是一行内容
文件对象.readlines()

'''

with open('文件/1.txt', 'r', encoding='utf-8') as f:
    print(f.readline())          # 000
    print(f.readline())          # 111


with open('文件/1.txt', 'r', encoding='utf-8') as f:
    # 一次读取所有行,返回值是列表,每一项都是一行内容
    res = f.readlines()
    print(res)           # ['000\n', '111\n', '222\n', '333\n', '444\n', '555\n', '666\n', '777\n', '888\n', '999\n', '\n']

# 去除前后换行符和空格,去掉空行
res = [i.strip() for i in res if len(i.strip()) > 0]
print(res)              # ['000', '111', '222', '333', '444', '555', '666', '777', '888', '999']


with open('文件/1.txt', 'r', encoding='utf-8') as f:
    # 读取全部,按行分隔,自动删除换行符
    res = f.read().splitlines()
    print(res)          # ['000', '111', '222', '333', '444', '555', '666', '777', '888', '999', '']
