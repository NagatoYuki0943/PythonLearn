'''
多核心占满
'''

import multiprocessing


def test():
    while True:
        pass


# 子进程死循环
processing = multiprocessing.Process(target=test)
processing.start()


# 主进程死循环
while True:
    pass