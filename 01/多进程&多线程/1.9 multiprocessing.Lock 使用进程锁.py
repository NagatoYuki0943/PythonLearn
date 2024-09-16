"""
lock在不同进程使用同一共享内存时，能够确保进程之间互不影响，使用lock的方法是，
在每个进程执行运算修改共享内存之前，执行lock.acquire()将共享内存上锁，
确保当前进程执行时，内存不会被其他进程访问，执行运算完毕后，
使用lock.release()将锁打开，保证其他的进程可以使用该共享内存。
"""

dummy = False
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
    for i in range(10):
        A += 1
        print("job1", A)
    lock.release()


def job2():
    global A, lock
    lock.acquire()
    for i in range(10):
        A += 10
        print("job2", A)
    lock.release()


def run_process():
    t1 = Process(target=job1)
    t2 = Process(target=job2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    # 结果很清晰,job1使用的时候会上锁,防止资源被job2占用,job1使用之后才给job2使用
    # job1 1
    # job1 2
    # job1 3
    # job1 4
    # job1 5
    # job1 6
    # job1 7
    # job1 8
    # job1 9
    # job1 10
    # job2 10
    # job2 20
    # job2 30
    # job2 40
    # job2 50
    # job2 60
    # job2 70
    # job2 80
    # job2 90
    # job2 100


if __name__ == "__main__":
    run_process()
