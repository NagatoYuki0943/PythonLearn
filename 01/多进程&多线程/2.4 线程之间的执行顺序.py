'''
无序，由CPU调度决定某个线程先执行
'''

from threading import Thread, current_thread
import time


def task():
    '''打印当前线程对象'''
    time.sleep(1)
    print(current_thread())


def run_threads():

    for i in range(5):
        sub_thread = Thread(target=task)
        sub_thread.start()

    # 执行顺序不同
    #  类型    名字       状态
    # <Thread(Thread-4, started 22180)>
    # <Thread(Thread-3, started 4284)>
    # <Thread(Thread-1, started 3164)>
    # <Thread(Thread-2, started 13848)>
    # <Thread(Thread-5, started 17216)>


if __name__ == '__main__':
    run_threads()
