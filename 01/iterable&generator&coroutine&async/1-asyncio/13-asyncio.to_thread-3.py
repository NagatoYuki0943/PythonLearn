# asyncio.to_thread() 可以把同步阻塞函数丢到线程里，避免卡住事件循环；
# 但因为 GIL，它通常主要适合 I/O 阻塞函数，不适合普通 Python CPU 密集计算，除非扩展模块释放 GIL 或使用无 GIL/替代实现。


import time
from typing import Any
import asyncio


_GENERATOR_END = object()


def blocking_io():
    for i in range(5):
        yield i
        time.sleep(1)  # 模拟 I/O 阻塞


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

        # 通过 to_thread 实现迭代返回, 避免阻塞事件循环
        generator = await asyncio.to_thread(blocking_io)
        iterator = iter(generator)
        while True:
            item = await asyncio.to_thread(next, iterator, _GENERATOR_END)
            if item is _GENERATOR_END:
                break
            print(item)

    print(f"finished at {time.strftime('%X')}")

    # started at 09:14:28
    # 0
    # 1
    # world - 1 seconds
    # 2
    # hello - 2 seconds
    # 3
    # 4
    # finished at 09:14:33


if __name__ == "__main__":
    asyncio.run(main())
