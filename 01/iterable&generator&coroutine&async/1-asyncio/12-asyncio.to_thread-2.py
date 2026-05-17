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

    async with asyncio.TaskGroup() as task_group:
        task_group.create_task(say_after(2, "hello"))
        task_group.create_task(say_after(1, "world"))

        # 想要和 TaskGroup 里的任务并发执行，必须在 TaskGroup 上下文里调用 to_thread()，否则会等 TaskGroup 里的任务完成才执行 to_thread()，就没并发了。
        result = await asyncio.to_thread(blocking_io)

    print(result)
    print(f"finished at {time.strftime('%X')}")

    # started at 19:46:22
    # world - 1 seconds
    # hello - 2 seconds
    # blocking_io done - 3 seconds
    # blocking_io result
    # finished at 19:46:25
    # 用时3秒, 实现并发


if __name__ == "__main__":
    asyncio.run(main())
