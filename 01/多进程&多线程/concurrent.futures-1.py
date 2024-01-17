from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import time


def sing(name: str, num: int) -> str:
    for i in range(num):
        print(f"{name}在唱歌。。。")
        time.sleep(0.5)
    return f"{name}-{num}"


def dance(name: str, num: int) -> str:
    for i in range(num):
        print(f"{name}跳舞。。。")
        time.sleep(0.5)
    return f"{name}-{num}"


if __name__ == "__main__":
    # 多进程要在 `if __name__ == "__main__"` 中进行,在ipynb中运行失败
    # with语句会调用executor.shutdown(wait=True)，在所有线程都执行完毕前阻塞当前线程
    with ProcessPoolExecutor(max_workers=3) as executor:
        future = executor.submit(sing, 'Yuki', 3)
        print(future.result())
        future = executor.submit(dance, name='Nagato', num=4)
        print(future.result())
