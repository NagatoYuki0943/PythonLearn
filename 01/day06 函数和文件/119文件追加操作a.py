"""
1.打开文件,将文件从硬盘存到内存中
open(file, mode='r', ..., encoding=None)
    file:       文件名
    model:      文件打开方式 r:读  w:写  a:append追加
        'r'       读,文件不存在报错
        'w'       删除文件内容(truncate)再写入,文件不存在会创建文件
        'x'       创建新文件并用写模式打开
        'a'       打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
        'b'       二进制模式
        't'       text mode (default)
        '+'       打开一个文件进行更新(可读可写)
        'U'       通用换行模式（不推荐）

写操作用的都是write()函数

"""

# 打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
f = open("文件/1.txt", "a", encoding="utf-8")

f.write("你真牛逼\n")


f.close()
