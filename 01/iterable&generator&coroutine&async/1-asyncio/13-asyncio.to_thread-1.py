# asyncio.to_thread() 可以把同步阻塞函数丢到线程里，避免卡住事件循环；
# 但因为 GIL，它通常主要适合 I/O 阻塞函数，不适合普通 Python CPU 密集计算，除非扩展模块释放 GIL 或使用无 GIL/替代实现。


import time
from typing import Any
import asyncio


def blocking_io():
    time.sleep(3)
    print("blocking_io done - 3 seconds")
    return "blocking_io result"


async def say_after(delay: float, what: Any):
    # asyncio.sleep() 会挂起当前协程，把控制权交还给事件循环；
    # 当前任务会在 delay 秒后恢复执行。
    await asyncio.sleep(delay)
    print(f"{what} - {delay} seconds")


async def main() -> None:
    print(f"started at {time.strftime('%X')}")

    task1 = asyncio.create_task(say_after(2, "hello"))
    task2 = asyncio.create_task(say_after(1, "world"))

    result = await asyncio.to_thread(blocking_io)
    await task1
    await task2

    print(result)
    print(f"finished at {time.strftime('%X')}")

    # started at 18:34:35
    # world - 1 seconds
    # hello - 2 seconds
    # blocking_io done - 3 seconds
    # blocking_io result
    # finished at 18:34:38
    # 用时3秒, 实现并发


if __name__ == "__main__":
    asyncio.run(main())
