from threading import Thread
from queue import (
    Queue,
)  # 线程安全的Queue, from multiprocessing import Queue 的Queue是进程安全的,更复杂
# from multiprocessing.dummy import Queue # 这个也是线程 Queue

"""
线程安全的Queue

对于 一个生产者，多个消费者，只有消费者直到最终任务什么时候结束，因此通过它来判断线程是否结束

在每一次往Queue中添加数据后，需要调用，python会在queue内部计数器+1
而 queue.task_done() 会让计数器减1
queue.join() 会阻塞，直到queue内部计数器减为0
"""


def consumer(queue: Queue):
    while True:
        data = queue.get()
        print("consumer:", data)
        # queue.task_done() 会让计数器减1
        queue.task_done()


def producer(queue: Queue):
    for i in range(10):
        queue.put(i)


queue = Queue()

# daemon=True 当主线程退出时，子线程也会退出
t1 = Thread(target=consumer, args=(queue,), daemon=True)
t2 = Thread(target=consumer, args=(queue,), daemon=True)

t1.start()
t2.start()

producer(queue)

# queue.join() 会阻塞，直到queue内部计数器减为0
queue.join()
