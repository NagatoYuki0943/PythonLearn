'''
1. 用只读的方式,打开文件
2. 读取文件内容
3. 关闭文件
4. 只写的方式,打开新文件
5. 将 第 2 步读取的内容写入新文件
6. 关闭新文件

思考:
    1. 如果文件比较大,循环读取文件
    2. 复制备份的文件可能是 txt 文件,可能是 二进制文件,  ---> 使用二进制方式打开文件比较好
    r   w   a
    rb  wb  ab
'''
# 输入文件名
filename = input('请输入要备份的文件名:')

f = open(filename, 'rb')
buf = f.read()
f.close()

# 根据原文件名找到后缀和文件名
index = filename.rfind('.')
# 文件后缀
suffix = filename[index::]     # .txt
# 文件名
name = filename[:index:]
# 新文件名
new_filename = name + '.备份' + suffix

print(new_filename)     # 输入: 文件/1.txt   输出: 文件/1.备份.txt


f = open(new_filename, 'wb')
f.write(buf)
f.close()
