"""
无论是直接调用函数还是在类里面调用函数,都是在外层创建txt文件
"""

from utils.Train import Train


def get_train():
    return Train()
