# asyncio.TaskGroup 是 Python 3.11 加入的现代写法，退出上下文时会隐式等待子任务结束；
# 相比 gather()，它在子任务异常时有更强的安全保证，会取消剩余任务，而 gather() 默认不会取消其他 awaitable，真是终于不像把异常扔进风里假装没事了。


import time
from typing import Any
import asyncio


async def say_after(delay: float, what: Any):
    # asyncio.sleep() 会挂起当前协程，把控制权交还给事件循环；
    # 当前任务会在 delay 秒后恢复执行。
    await asyncio.sleep(delay)
    return f"{what} - {delay} seconds"


async def main():
    print(f"started at {time.strftime('%X')}")

    async with asyncio.TaskGroup() as task_group:
        t1 = task_group.create_task(say_after(2, "hello"))
        t2 = task_group.create_task(say_after(1, "world"))

        # 这里 main() 函数挂起了, 把控制权交还给 event loop, 于是 event loop 就可以调度 task1 和 task2 这两个任务了
        await asyncio.sleep(2)

    # 退出 TaskGroup 时，里面的任务都已完成
    print(t1.result())
    print(t2.result())

    print(f"finished at {time.strftime('%X')}")

    # started at 17:40:37
    # hello - 2 seconds
    # world - 1 seconds
    # finished at 17:40:39
    # 相差2秒, 实现并发


if __name__ == "__main__":
    asyncio.run(main())
