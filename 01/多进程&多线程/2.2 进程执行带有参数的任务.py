"""
传递参数:
    args:   以元组的方式给执行任务传参
        注意: (1,) 元组一个数据也要加逗号
    kwargs: 以字典方式给执行任务传参
"""

from threading import Thread
import time


def sing(name: str, num: int):
    for i in range(num):
        print(f"{name}在唱歌。。。")
        time.sleep(0.5)


def dance(name: str, num: int):
    for i in range(num):
        print(f"{name}跳舞。。。")
        time.sleep(0.5)


def run_threads():
    # 以元组形式传参                (1,) 元组一个数据也要加逗号
    s1 = Thread(target=sing, args=("Yuki", 3))

    # 以字典形式传参
    d1 = Thread(target=dance, kwargs={"name": "Nagato", "num": 4})
    s1.start()
    d1.start()

    s1.join()
    d1.join()

    # Nagato跳舞。。。
    # Yuki在唱歌。。。
    # Yuki在唱歌。。。
    # Nagato跳舞。。。
    # Yuki在唱歌。。。
    # Nagato跳舞。。。
    # Nagato跳舞。。。


if __name__ == "__main__":
    run_threads()
