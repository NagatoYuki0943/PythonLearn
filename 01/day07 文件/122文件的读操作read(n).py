'''
def read(self, n: int = ...)
n: 一次性读取多少字节的内容,默认不写读取全部内容

读写文件
    一次读取文件中的所有内容,返回文件内容
    文件对象.read(n)
    n: 一次性读取多少字节的内容,默认不写读取全部内容
    读到文件末尾会返回None
        buff = f.read()

'''

f = open('文件/1.txt', 'r', encoding='utf-8')


# n: 一次性读取多少字节的内容,默认不写读取全部内容
res = f.read(3)
print(res)          # 111
print('*' * 20)
res = f.read(3)     # 换行和22
print(res)


f.close()


