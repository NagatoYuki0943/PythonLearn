'''
# 创建多任务               函数名
t1 = threading.Thread(target=sing)

# 启动多线程
t1.start()

# 等待子线程执行完毕
t1.join()
'''

from threading import Thread
import time


def sing():
    for i in range(3):
        print("唱歌。。。")
        time.sleep(0.5)


def dance():
    for i in range(3):
        print("跳舞。。。")
        time.sleep(0.5)


def run_threads():
    start = time.time()

    # 创建多任务 函数名
    t1 = Thread(target=sing)
    t2 = Thread(target=dance)

    # 多线程下run方法启动相当于直接调用函数，并没有真正意义上使用多线程，这一点我们可以通过pid看的出来。而start启动却是真正意义上调用了多线程，同样我们可以通过pid看的出来
    # t1.run()

    # 启动多线程
    t1.start()
    t2.start()

    # 等待子线程执行完毕
    t1.join()
    t2.join()

    print('Interval:', time.time() - start)
    # 唱歌。。。
    # 跳舞。。。
    # 唱歌。。。
    # 跳舞。。。
    # 唱歌。。。
    # 跳舞。。。
    # Interval: 1.5247292518615723


if __name__ == '__main__':
    run_threads()

