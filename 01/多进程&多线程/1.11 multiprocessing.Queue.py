dummy = False
if dummy:
    # 线程
    from multiprocessing.dummy import Process, Pool, Queue, Pipe, Lock
else:
    # 进程
    from multiprocessing import Process, Pool, Queue, SimpleQueue, Pipe, Lock
from queue import Empty
import time


"""2个进程使用同一个queue通信
"""


def process1(queue: Queue):
    for i in range(5):
        # 阻塞等待,直到有空闲槽
        queue.put(i)
        time.sleep(0.5)
    queue.put(None)


def process2(queue: Queue):
    while True:
        # 阻塞等待,超时时间单位为秒
        data = queue.get(timeout=None)
        print(data)
        if data is None:
            queue.close()
            return


def run_queue():
    queue = Queue(maxsize=3)
    p1 = Process(target=process1, args=(queue,))
    p2 = Process(target=process2, args=(queue,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    # 0
    # 1
    # 2
    # 3
    # 4
    # Empty


if __name__ == "__main__":
    run_queue()
