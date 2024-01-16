'''
默认情况下 主进程会等待所有的子进程执行结束在结束,下面会继续执行子进程(就继续打印)
不想这样的话就设置守护进程,主进程结束后会停止所有子进程
daemon=True
'''

dummy = False
if dummy:
    # 线程
    from multiprocessing.dummy import Process, Pool, Queue, Pipe, Lock
else:
    # 进程
    from multiprocessing import Process, Pool, Queue, Pipe, Lock
import time


def work():
    for i in range(10):
        print("工作中。。。。")
        time.sleep(0.2)


def run_process():
    # 设置守护主进程  daemon=True
    # 主进程结束后不会再继续执行子进程中剩余的工作
    work_process = Process(target=work, daemon=True)
    # 写法2
    # work_process.daemon = True

    work_process.start()

    time.sleep(1)
    print("主进程执行结束")
    # 默认情况下 主进程会等待所有的子进程执行结束在结束,下面会继续执行子进程(就继续打印)

    # 工作中。。。。
    # 工作中。。。。
    # 工作中。。。。
    # 工作中。。。。
    # 工作中。。。。
    # 主进程执行结束


if __name__ == "__main__":
    run_process()
