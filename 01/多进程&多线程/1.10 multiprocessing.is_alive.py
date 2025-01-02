"""
lock在不同进程使用同一共享内存时，能够确保进程之间互不影响，使用lock的方法是，
在每个进程执行运算修改共享内存之前，执行lock.acquire()将共享内存上锁，
确保当前进程执行时，内存不会被其他进程访问，执行运算完毕后，
使用lock.release()将锁打开，保证其他的进程可以使用该共享内存。
"""
import time

dummy = False
if dummy:
    # 线程
    # 这里的 Queue 等同于 `from queue import Queue`, 是线程安全的, 有 task_done 和 join 方法
    from multiprocessing.dummy import Process, Pool, Queue, Pipe, Lock
else:
    # 进程
    # 这里的 Queue 是进程安全的
    from multiprocessing import Process, Pool, Queue, Pipe, Lock


A = 0
lock = Lock()


def job1():
    global A, lock
    lock.acquire()
    for i in range(5):
        A += 1
        print("job1", A)
        time.sleep(0.5)
    lock.release()


def job2():
    global A, lock
    lock.acquire()
    for i in range(5):
        A += 10
        print("job2", A)
        time.sleep(0.5)
    lock.release()


def run_process():
    t1 = Process(target=job1)
    t2 = Process(target=job2)
    time.sleep(1)
    print(t1.is_alive(), t2.is_alive())
    # False False

    t1.start()
    t2.start()
    print(t1.is_alive(), t2.is_alive())
    # True True
    time.sleep(1)

    t1.join()
    t2.join()
    print(t1.is_alive(), t2.is_alive())
    # False False


if __name__ == "__main__":
    run_process()
