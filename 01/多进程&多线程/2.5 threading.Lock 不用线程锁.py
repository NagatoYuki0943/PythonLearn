from threading import Thread, Lock


A = 0

def job1():
    global A
    for i in range(10):
        A += 1
        print('job1',A)


def job2():
    global A
    for i in range(10):
        A += 10
        print('job2',A)


def run_threads():
    t1 = Thread(target=job1)
    t2 = Thread(target=job2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    # 结果很乱,2个线程相互争夺资源,没有顺序
    # job1 1
    # job1 2
    # job2 12
    # job1 13
    # job2 23
    # job1 24
    # job2 34
    # job1 35
    # job2 45
    # job1 46
    # job2 56
    # job1 57
    # job2 67
    # job1 68
    # job2 78
    # job1 79
    # job2 89
    # job1 90
    # job2 100
    # job2 110


if __name__ == '__main__':
    run_threads()
