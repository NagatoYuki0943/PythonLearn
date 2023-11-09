'''
# 创建进程池                          进程数
pool = multiprocessing.Pool(processes=2)

# 主进程会被阻塞直到函数执行结束(同步,不建议使用)
pool.apply(func=sing, args=('Yuki', 3))
pool.apply(func=dance, kwds={'name': 'Nagato', 'num': 4})

# 非阻塞的且支持结果返回后进行回调(异步)
pool.apply_async(func=sing, args=('Yuki', 3))
pool.apply_async(func=dance, kwds={'name': 'Nagato', 'num': 4})

# 将多组参数传递给一个函数,生成多个进程,使进程阻塞直到结果返回
pool.map(func=sing, iterable=argss)

# 将多组参数传递给一个函数,生成多个进程,非阻塞
pool.map_async(func=sing, iterable=argss)

# 关闭进程池,要在 join 之前
pool.close()

# 等待子进程执行完毕
pool.join()

# 结束工作进程，不再处理未处理的任务
pool.terminate()
'''

from multiprocessing import Pool
import time


def sing(name: str, num: int):
    for i in range(num):
        print(f"{name}在唱歌。。。")
        time.sleep(0.5)


def dance(name: str, num: int):
    for i in range(num):
        print(f"{name}跳舞。。。")
        time.sleep(0.5)


if __name__ == '__main__':
    start = time.time()

    pool = Pool(processes=2)

    # 主进程会被阻塞直到函数执行结束(同步,不建议使用)
    # pool.apply(func=sing, args=('Yuki', 3))
    # pool.apply(func=dance, kwds={'name': 'Nagato', 'num': 4})

    # 非阻塞的且支持结果返回后进行回调(异步)
    pool.apply_async(func=sing, args=('Yuki', 3))
    pool.apply_async(func=dance, kwds={'name': 'Nagato', 'num': 4})

    # join之前有close
    pool.close()
    # pool.terminate()
    # 等待子进程执行完毕
    pool.join()
    # 结束工作进程，不再处理未处理的任务
    pool.terminate()

    print('Interval:', time.time() - start)
    # Yuki在唱歌。。。
    # Nagato跳舞。。。
    # Yuki在唱歌。。。
    # Nagato跳舞。。。
    # Yuki在唱歌。。。
    # Nagato跳舞。。。
    # Nagato跳舞。。。
    # Interval: 2.116147518157959
