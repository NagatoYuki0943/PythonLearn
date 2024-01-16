dummy = False
if dummy:
    # 线程
    from multiprocessing.dummy import Process, Pool, Queue, Pipe, Lock
else:
    # 进程
    from multiprocessing import Process, Pool, Queue, SimpleQueue, Pipe, Lock
from multiprocessing.connection import Connection, PipeConnection
from queue import Empty
import time


"""2个进程使用同pipe通信
"""


def process1(conn: PipeConnection):
    x = 1

    while True:
        conn.send(x + 1)
        x = conn.recv()
        print(x)
        time.sleep(1)


def process2(conn: PipeConnection):
    while True:
        x = conn.recv()
        print(x)
        conn.send(x + 2)
        time.sleep(1)


def run_queue():
    conn1, conn2 = Pipe(duplex=True)
    p1 = Process(target=process1, args=(conn1, ))
    p2 = Process(target=process2, args=(conn2, ))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    # 2
    # 4
    # 5
    # 7
    # 8
    # 10
    # 11
    # 13
    # 14
    # 16
    # 17
    # 19
    # 20

if __name__ =='__main__':
    run_queue()
