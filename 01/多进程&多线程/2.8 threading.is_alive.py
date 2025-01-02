"""
# 创建多任务               函数名
t1 = threading.Thread(target=sing)

# 启动多线程
t1.start()

# 等待子线程执行完毕
t1.join()
"""

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
    # 创建多任务 函数名
    t1 = Thread(target=sing)
    t2 = Thread(target=dance)
    time.sleep(1)
    print(t1.is_alive(), t2.is_alive())
    # False False

    # 启动多线程
    t1.start()
    t2.start()
    print(t1.is_alive(), t2.is_alive())
    # True True
    time.sleep(1)

    # 等待子线程执行完毕
    t1.join()
    t2.join()
    print(t1.is_alive(), t2.is_alive())
    # False False


if __name__ == "__main__":
    run_threads()
