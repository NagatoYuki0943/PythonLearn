'''
子线程使用C语言函数
'''
from threading import Thread

# 1.导入模块 ctype
import ctypes


# 2.加载so文件 (linux上创建)
my_lib = ctypes.cdll.LoadLibrary('./libstest.so')


# 3.创建子线程       C语言中的函数
threads = Thread(target=my_lib.Loop)
threads.start()


# 4.主线程死循环
while True:
    pass




