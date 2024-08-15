'''
默认情况下 主线程会等待所有的子线程执行结束在结束,下面会继续执行子线程(就继续打印)
不想这样的话就设置守护线程,主线程结束后会停止所有子线程
daemon=True
'''

import time
from threading import Thread


def work():
    for i in range(10):
        print("工作中。。。。")
        time.sleep(0.2)


def run_threads():
    # 设置守护线程,主线程结束后会停止所有子线程
    work_process = Thread(target=work, daemon=True)
    # 两种写法相同
    # work_process.daemon = True

    work_process.start()

    time.sleep(1)
    print("主线程执行结束")
    # 默认情况下 主线线程会等待所有的子线程执行结束在结束,下面会继续执行子线程(就继续打印)

    # 工作中。。。。
    # 工作中。。。。
    # 工作中。。。。
    # 工作中。。。。
    # 工作中。。。。
    # 主线程执行结束


if __name__ == '__main__':
    run_threads()

