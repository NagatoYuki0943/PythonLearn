dummy = False
if dummy:
    # 线程
    from multiprocessing.dummy import Process, Pool, Queue, Pipe, Lock
else:
    # 进程
    from multiprocessing import Process, Pool, Queue, SimpleQueue, Pipe, Lock
from multiprocessing.connection import Connection, PipeConnection


def run_queue():
    queue = Queue(maxsize=3)

    # 是否为空
    print(queue.empty())  # True

    # Put an item into the queue.
    # 如果可选参数 'block' 为 true 并且 'timeout' 为 None （默认值），则根据需要进行阻止，直到有空闲槽可用。
    # 如果"timeout"是非负数，则它最多会阻塞"timeout"秒，并且如果在该时间内没有可用的空闲槽，则会引发 Full 异常。
    # 否则（"block"为 false），如果空闲槽立即可用，则将项目放入队列中，否则引发 Full 异常（在这种情况下忽略"timeout"）。
    queue.put(True, block=True)
    queue.put([0, None, object])  # you can put deepcopy thing

    # 是否满了
    print(queue.full())  # False

    # 目前队列数量
    print(queue.qsize())  # 2

    # 等同于 `queue.put(obj, False)`
    queue.put_nowait("a")

    print(queue.empty())  # False
    print(queue.full())  # True
    print(queue.qsize())  # 3

    # 从队列中取出一个元素
    # 从队列中删除并返回一个项目。 如果可选参数块是（默认）并且超时是（默认），则根据需要进行阻止，直到有项目可用。
    # 如果超时是正数，则它最多会阻塞超时秒并引发队列。如果在该时间内没有可用的项目，则会引发空异常。 否则（块是），
    # 如果一项立即可用，则返回一项，否则引发队列空异常（在这种情况下超时被忽略）。`True None False``
    print(queue.get(block=True))  # True
    print(queue.get())  # [0, None, <class 'object'>]

    # 等同于 `queue.get(False)`
    print(queue.get_nowait())  # a

    print(queue.qsize())  # 0

    print(queue.empty())  # True

    # 表明当前进程不会再向此队列放入更多数据。 一旦将所有缓冲数据刷新到管道，后台线程就会退出。 当队列被垃圾收集时，会自动调用此函数。
    queue.close()

    # 加入后台线程。 这只能在调用 close() 后使用。 它会阻塞直到后台线程退出，确保缓冲区中的所有数据都已刷新到管道。
    queue.join_thread()


def run_simple_queue():
    """It is a simplified Queue type, very close to a locked Pipe."""
    queue = SimpleQueue()

    print(queue.empty())  # True
    queue.put("A")
    queue.put("B")
    print(queue.empty())  # False
    print(queue.get())  # A
    print(queue.get())  # B
    print(queue.empty())  # True

    # Close the queue
    queue.close()


def run_pipe():
    """双工的Pipe
    conn1.send(object) -> conn2.recv()
    conn2.send(object) -> conn1.recv()
    """
    conn1: PipeConnection
    conn2: PipeConnection
    conn1, conn2 = Pipe(duplex=True)

    # conn1 send and conn2 recv
    conn1.send("a")
    conn1.send("b")
    print(conn2.recv())  # a
    print(conn2.recv())  # b

    # conn2 send and conn1 recv
    conn2.send(1)
    conn2.send(2)
    print(conn1.recv())  # 1
    print(conn1.recv())  # 2

    print(conn1.readable)  # True  是否可读
    print(conn1.writable)  # True  是否可写入
    print(conn1.closed)  # False 是否关闭
    conn1.close()
    conn2.close()
    print(conn1.readable)  # True
    print(conn1.writable)  # True
    print(conn1.closed)  # True


if __name__ == "__main__":
    run_queue()
    print("-" * 10)
    run_simple_queue()
    print("-" * 10)
    run_pipe()
