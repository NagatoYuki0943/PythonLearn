"""
无论是直接调用函数还是在类里面调用函数,都是在外层创建txt文件
"""

from utils.function import loss_write


class Train(object):
    def __init__(self) -> None:
        loss_write(1)
