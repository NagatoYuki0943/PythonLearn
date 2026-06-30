# asyncio.to_thread() 可以把同步阻塞函数丢到线程里，避免卡住事件循环；
# 但因为 GIL，它通常主要适合 I/O 阻塞函数，不适合普通 Python CPU 密集计算，除非扩展模块释放 GIL 或使用无 GIL/替代实现。


import time
from typing import Any
import asyncio


def blocking_io():
    for i in range(5):
        yield i
        time.sleep(1)

    return "blocking_io finished"


def next_with_return(iterator):
    try:
        item = next(iterator)
        return False, item
    except StopIteration as exc:
        return True, exc.value


async def say_after(delay: float, what: Any):
    await asyncio.sleep(delay)
    print(f"{what} - {delay} seconds")


async def main() -> None:
    print(f"started at {time.strftime('%X')}")

    result = None

    async with asyncio.TaskGroup() as task_group:
        task_group.create_task(say_after(2, "hello"))
        task_group.create_task(say_after(1, "world"))

        iterator = iter(blocking_io())

        # 这样可以获取 blocking_io return value
        while True:
            done, value = await asyncio.to_thread(next_with_return, iterator)

            if done:
                result = value
                break

            print(value)

    print(f"generator return value: {result}")
    print(f"finished at {time.strftime('%X')}")

    # started at 09:37:03
    # 0
    # world - 1 seconds
    # 1
    # hello - 2 seconds
    # 2
    # 3
    # 4
    # generator return value: blocking_io finished
    # finished at 09:37:08


if __name__ == "__main__":
    asyncio.run(main())
