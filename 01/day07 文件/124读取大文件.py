'''
read() 一次读取全部内容
read() 读到文件末尾会返回None
'''

# 有换行的大文件可以一行一行读
f = open('文件/1.txt', 'r', encoding='utf-8')
while True:
    buf = f.readline()
    if buf: # 有数据为True,没数据是False
        print(buf, end="")
    else:
        break
print('*' * 50)
f.close()


# 没有换行的文件
f = open('文件/2.txt', 'r', encoding='utf-8')
while True:
    buf = f.read(10)
    if buf: # 有数据为True,没数据是False
        print(buf, end=" ")
    else:
        break