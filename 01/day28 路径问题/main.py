'''
python中使用不同目录的函数,
函数的相对路径是调用时调用文件的路径,不是被调用文件的路径

'''


from utils.function import loss_write
import os
import sys
os.chdir(sys.path[0])

if __name__ == "__main__":
    loss_write(1)