import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, TimeoutError
from contextlib import contextmanager


@@ -9,7 +8,7 @@ def executor_context(max_workers: int = 1, type: str = "thread"):
    工作原理
        1. 资源创建：首先创建 ThreadPoolExecutor 实例。
        2. try 块：yield 语句将 executor 传递给上下文管理器的用户代码。这允许在 with 语句块中使用线程池/进程池。
        3. finally 块：无论执行过程中是否发生异常，finally 块都会执行，确保：
            - 取消所有待处理的任务
            - 安全关闭线程池
@@ -38,30 +37,3 @@ def executor_context(max_workers: int = 1, type: str = "thread"):

        # b. 使用wait=True确保所有线程都已完成
        executor.shutdown(wait=True)
def sing(num):
    """唱歌"""
    for i in range(num):
        time.sleep(0.2)
        print(f"唱歌{num}")
    print(f"唱完了{num}")
def dance(num):
    """跳舞"""
    for i in range(num):
        time.sleep(0.2)
        print(f"跳舞{num}")
    print(f"跳完了{num}")
def test_executor_context():
    with executor_context(max_workers=2) as executor:
        for i in range(10):
            executor.submit(sing, i)
            executor.submit(dance, i)
if __name__ == "__main__":
    test_executor_context()
