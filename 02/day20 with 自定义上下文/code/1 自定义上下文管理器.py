'''
自定义上下文管理器实现文件操作 满足 with操作
类: MyFile()
类方法:
    __init__()   接收参数,并且初始化
    __enter__()  上文方法  with开始调用
    __exit__()   下文方法  with结束调用

with MyFile('hello.txt', 'r') as file

'''
import os
import sys
os.chdir(sys.path[0])


class MyFile(object):
    def __init__(self, file_name, mode='r', encoding='utf-8') -> None:
        self.file_name = file_name
        self.mode = mode
        self.encoding = encoding


    # 上文方法 with开始调用
    def __enter__(self):
        print("进入上文")
        self.file = open(self.file_name, self.mode, encoding=self.encoding)
        return self.file


    # 下文方法 with结束调用 必须有四个参数
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("进入下文")
        self.file.close()


with MyFile('hello.txt', 'r', 'utf-8') as file:
    lines = file.readlines()
    print(lines)
    # 进入上文
    # ['nihao,zaima\n', 'buhao,zaijian']
    # 进入下文
