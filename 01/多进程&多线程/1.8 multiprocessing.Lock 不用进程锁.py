dummy = False
if dummy:
    # 线程
    from multiprocessing.dummy import Process, Pool, Queue, Pipe, Lock
else:
    # 进程
    from multiprocessing import Process, Pool, Queue, Pipe, Lock


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


def run_process():
    t1 = Process(target=job1)
    t2 = Process(target=job2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    # 结果很清晰,理应很乱,在多线程中是乱的,在进程中就很正常,和使用了lock一样,原因不明
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


if __name__== '__main__':
    run_process()
