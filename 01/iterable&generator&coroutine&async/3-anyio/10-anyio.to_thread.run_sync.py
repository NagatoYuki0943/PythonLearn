# anyio.to_thread.run_sync() 同步阻塞函数丢线程


import time
from typing import Any
import anyio
from anyio import to_thread


def blocking_io():
    time.sleep(3)
    print("blocking_io done - 3 seconds")
    return "blocking_io result"


async def say_after(delay: float, what: Any):
    # asyncio.sleep() 会挂起当前协程，把控制权交还给事件循环；
    # 当前任务会在 delay 秒后恢复执行。
    await anyio.sleep(delay)
    print(f"{what} - {delay} seconds")


async def main() -> None:
    print(f"started at {time.strftime('%X')}")

    result: str | None = None

    async with anyio.create_task_group() as task_group:
        task_group.start_soon(say_after, 2, "hello")
        task_group.start_soon(say_after, 1, "world")

        # 想要和 task_group 中的其他任务并发执行，就要在 task_group 的上下文中调用 anyio.to_thread.run_sync
        result = await to_thread.run_sync(blocking_io)

    print(result)
    print(f"finished at {time.strftime('%X')}")

    # started at 21:10:07
    # world - 1 seconds
    # hello - 2 seconds
    # blocking_io done - 3 seconds
    # blocking_io result
    # finished at 21:10:10
    # 用时3秒, 实现并发


if __name__ == "__main__":
    anyio.run(main)
