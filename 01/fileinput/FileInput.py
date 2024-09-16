"""
FileInput 必须以 r rb rU U 模式打开,只能读取,不能写入
FileInput可以使用fileinput中的大量方法
"""

import fileinput
from fileinput import FileInput

path = "./fileinput1.txt"


# 将一个文件中所有的行提取到一个列表中
# files = list(FileInput(path))

print("open:")
with open(path, mode="r", encoding="utf-8") as files:
    lines = files.readlines()
    for line in lines:
        # 打印每一行
        print(line, end="")
print("*" * 50)


# FileInput可以同时打印多个文件
path = ["./fileinput1.txt", "./fileinput2.txt"]
files = FileInput(path, mode="r")
for l in list(files):
    # 打印每一行
    print(l, end="")
print("*" * 50)
# 读取一行
print(files.readline())
# 获取文件名
print(files.filename())
# files.filename()

files.close()
