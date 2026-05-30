# trio.to_thread.run_sync() 同步阻塞函数丢线程


import time
from typing import Any
import trio


def blocking_io():
    time.sleep(3)
    print("blocking_io done - 3 seconds")
    return "blocking_io result"


async def say_after(delay: float, what: Any):
    # asyncio.sleep() 会挂起当前协程，把控制权交还给事件循环；
    # 当前任务会在 delay 秒后恢复执行。
    await trio.sleep(delay)
    print(f"{what} - {delay} seconds")


async def main() -> None:
    print(f"started at {time.strftime('%X')}")

    async with trio.open_nursery() as nursery:
        nursery.start_soon(say_after, 2, "hello")
        nursery.start_soon(say_after, 1, "world")

        # 想要和 nursery 中的其他任务并发执行，就要在 nursery 的上下文中调用 trio.to_thread.run_sync
        result = await trio.to_thread.run_sync(blocking_io)

    print(result)
    print(f"finished at {time.strftime('%X')}")

    # started at 19:48:27
    # world - 1 seconds
    # hello - 2 seconds
    # blocking_io done - 3 seconds
    # blocking_io result
    # finished at 19:48:30
    # 用时3秒, 实现并发


if __name__ == "__main__":
    trio.run(main)
