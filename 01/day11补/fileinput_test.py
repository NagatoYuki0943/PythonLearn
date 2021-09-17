import os

from fileinput import FileInput

path = './assert.py'


# 将一个文件中所有的行提取到一个列表中
# files = list(FileInput(path))

print('open:')
with open(path, mode='r', encoding='utf-8') as files:
    lines = files.readlines()
    for line in lines:
        print(line)
print('*' * 50)

files = list(FileInput(path))
print(files)