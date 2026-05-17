import time
from typing import Any
import asyncio


async def say_after(delay: float, what: Any):
    # asyncio.sleep() 会挂起当前协程，把控制权交还给事件循环；
    # 当前任务会在 delay 秒后恢复执行。
    await asyncio.sleep(delay)
    print(f"{what} - {delay} seconds")
    return f"{what} - {delay} seconds"


async def main():
    # create_task() 会把 coroutine 转换为一个 task 对象, 并将其注册到 event loop
    # 但是 event loop 并不会立即执行该 task, 以为当前控制权仍在 main() 函数中
    # main() 函数会继续创建另一个 task 对象, 并注册到 event loop
    task1 = asyncio.create_task(say_after(2, "hello"))
    task2 = asyncio.create_task(say_after(1, "world"))

    print(f"started at {time.strftime('%X')}")

    # 这里 main() 函数挂起了, 把控制权交还给 event loop, 于是 event loop 就可以调度 task1 和 task2 这两个任务了
    # 也就是说即使没有下面的 await 这行代码, 这两个任务也会被调度执行的
    await asyncio.sleep(2)

    # 1. await 后面是一个 task 对象, 是告诉 event loop 等待该 task 执行完毕
    # 2. 然后把控制权交给了 event loop, 直到该 task 执行完毕, 才会继续执行下面的代码
    # 3. 然后 main() 函数会 await 另一个 task 对象, 2个 task 并行执行, 并等待其执行完毕
    ret1 = await task1
    ret2 = await task2

    print(ret1)
    print(ret2)

    print(f"finished at {time.strftime('%X')}")

    # started at 13:10:55
    # hello - 2 seconds
    # world - 1 seconds
    # finished at 13:10:57
    # 相差2秒, 实现并发


if __name__ == "__main__":
    asyncio.run(main())
