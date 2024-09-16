""" """

import threading


def test():
    while True:
        pass


# 子进程死循环
thread = threading.Thread(target=test)
thread.start()


# 主进程死循环
while True:
    pass
