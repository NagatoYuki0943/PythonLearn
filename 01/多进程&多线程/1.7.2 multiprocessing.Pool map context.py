"""
# 创建进程池                          进程数
pool = multiprocessing.Pool(processes=2)

# 主进程会被阻塞直到函数执行结束(同步,不建议使用)
pool.apply(func=sing, args=('Yuki', 3))
pool.apply(func=dance, kwds={'name': 'Nagato', 'num': 4})

# 非阻塞的且支持结果返回后进行回调(异步)
pool.apply_async(func=sing, args=('Yuki', 3))
pool.apply_async(func=dance, kwds={'name': 'Nagato', 'num': 4})

# 将多组参数传递给一个函数,生成多个进程,使进程阻塞直到结果返回
# 每一组参数只能有1个参数
pool.map(func=sing, iterable=argss)

# 将多组参数传递给一个函数,生成多个进程,非阻塞
# 每一组参数只能有1个参数
pool.map_async(func=sing, iterable=argss)

# startmap 和 map 的差别是每一组参数可以传入多个参数
pool.startmap(func=sing, iterable=argss)

# startmap_async 和 map_async 的差别是每一组参数可以传入多个参数
pool.starmap_async(func=sing, iterable=argss)

# 关闭进程池,要在 join 之前
pool.close()

# 等待子进程执行完毕
pool.join()

# 结束工作进程，不再处理未处理的任务
pool.terminate()
"""

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


# 注意,这里传递的参数只有一个,传递多个的时候只有第一个参数接收到一个tuple
def sing(args):
    name: str = args[0]
    num: int = args[1]
    for i in range(num):
        print(f"{name}在唱歌。。。")
        time.sleep(0.5)


def run_process():
    start = time.time()

    argss = [("Yuki", 3), ("Nagato", 4)]

    with Pool(processes=2) as pool:
        # 将多组参数传递给一个函数,生成多个进程,使进程阻塞直到结果返回
        # context 要配合 map 使用,否则也需要使用 close 和 join 方法
        pool.map(func=sing, iterable=argss)

        # 将多组参数传递给一个函数,生成多个进程,非阻塞
        # pool.map_async(func=sing, iterable=argss)
        # join之前有close
        # pool.close()
        # pool.join()

    print("Interval:", time.time() - start)
    # Yuki在唱歌。。。
    # Nagato在唱歌。。。
    # Yuki在唱歌。。。
    # Nagato在唱歌。。。
    # Yuki在唱歌。。。
    # Nagato在唱歌。。。
    # Nagato在唱歌。。。
    # Interval: 2.116753578186035


if __name__ == "__main__":
    run_process()
