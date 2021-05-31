'''
模块注意点:
    自己定义的模块名字,不要和系统中你要使用的模块名字相同

搜索模块顺序 当前目录 --> 系统目录  ---> 程序报错

查看模块查找顺序
import sys
print(sys.path)

'''

import random


a = random.randint(1, 5)
print(a)


# 查看模块查找顺序
import sys
print(sys.path)