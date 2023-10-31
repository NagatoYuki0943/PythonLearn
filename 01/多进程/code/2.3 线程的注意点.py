'''
默认情况下 主线程会等待所有的子进程执行结束在结束,下面会继续执行子线程(就继续打印)
不想这样的话就设置守护进程,主线程结束后会停止所有子进程
daemon=True
'''

import time
import threading


def work():
    for i in range(10):
        print("工作中。。。。")
        time.sleep(0.2)


if __name__ == '__main__':
    # 设置守护进程,主线程结束后会停止所有子进程
    work_process = threading.Thread(target=work, daemon=True)
    # 两种写法相同
    # work_process.daemon = True

    work_process.start()

    time.sleep(1)
    print("主线程执行结束")
    # 默认情况下 主线进程会等待所有的子进程执行结束在结束,下面会继续执行子线程(就继续打印)

    # 工作中。。。。
    # 工作中。。。。
    # 工作中。。。。
    # 工作中。。。。
    # 工作中。。。。
    # 主进程执行结束
