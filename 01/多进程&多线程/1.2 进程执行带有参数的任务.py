'''
传递参数:
    args:   以元组的方式给执行任务传参
        注意: (1,) 元组一个数据也要加逗号
    kwargs: 以字典方式给执行任务传参
'''

dummy = False
if dummy:
    # 线程
    # 这里的 Queue 等同于 `from queue import Queue`, 是线程安全的, 有 task_done 和 join 方法
    from multiprocessing.dummy import Process, Pool, Queue, Pipe, Lock
else:
    # 进程
    # 这里的 Queue 是进程安全的
    from multiprocessing import Process, Pool, Queue, Pipe, Lock
import time


def sing(name: str, num: int):
    for i in range(num):
        print(f"{name}在唱歌。。。")
        time.sleep(0.5)


def dance(name: str, num: int):
    for i in range(num):
        print(f"{name}跳舞。。。")
        time.sleep(0.5)


def run_process():
    # 以元组形式传参                 (1,) 元组一个数据也要加逗号
    s1 = Process(target=sing, args=('Yuki', 3))

    # 以字典形式传参
    d1 = Process(target=dance, kwargs={'name': 'Nagato', 'num': 4})

    s1.start()
    d1.start()

    s1.join()
    d1.join()

    # Nagato跳舞。。。
    # Yuki在唱歌。。。
    # Yuki在唱歌。。。
    # Nagato跳舞。。。
    # Yuki在唱歌。。。
    # Nagato跳舞。。。
    # Nagato跳舞。。。


if __name__ == '__main__':
    run_process()
