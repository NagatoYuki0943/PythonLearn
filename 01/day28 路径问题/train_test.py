'''
python中使用不同目录的函数,
函数的相对路径是调用时调用文件的路径,不是被调用文件的路径
无论是直接调用函数还是在类里面调用函数,都是在外层创建txt文件
'''


from utils.function import loss_write
from utils.Train import Train
from utils.get_train import get_train
import os
import sys
os.chdir(sys.path[0])

if __name__ == "__main__":
    # loss_write(1)             # 在外层建立
    # train = Train()           # 在外层建立
    train = get_train()       # 在内层建立