from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from contextlib import contextmanager
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


# 使用 contextmanager 装饰器来创建线程池/进程池, 管理线程池/进程池的生命周期
# https://www.perplexity.ai/search/shang-mian-shi-yi-ge-shu-mei-p-zY6puYdZTcO8euQ1uVK0kg
# https://claude.ai/chat/2683b22b-c547-47fe-9b1c-65a9290926c8
@contextmanager
def executor_context(max_workers: int = 1):
    executor = ProcessPoolExecutor(max_workers=max_workers)
    try:
        yield executor
    finally:
        # 1. 首先尝试取消所有pending的任务
        for future in executor._threads:
            try:
                future.cancel()
            except Exception:
                pass

        # 2. 使用wait=True确保所有线程都已完成
        executor.shutdown(wait=True)


if __name__ == "__main__":
    # 多进程要在 `if __name__ == "__main__"` 中进行,在ipynb中运行失败
    # with语句会调用executor.shutdown(wait=True)，在所有线程都执行完毕前阻塞当前线程
    with executor_context(3) as executor:
        future = executor.submit(sing, "Yuki", 3)
        print(future.result())
        future = executor.submit(dance, name="Nagato", num=4)
        # 超时设置 10 秒，如果超过 10 秒还没有结果，则抛出 TimeoutError 异常
        print(future.result(timeout=10))
        # 尽可能地取消未完成的任务
        future.cancel()
