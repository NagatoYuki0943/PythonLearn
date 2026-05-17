# AnyIO 提供锁、条件变量、事件、信号量、对象流等任务间同步和通信工具；
# 普通“最多同时 N 个任务”用 Semaphore 很直观，资源配额类场景也可以用 CapacityLimiter。


import time
import anyio


async def expensive(i: int, sem: anyio.Semaphore) -> None:
    async with sem:
        print(f"start {i}")
        await anyio.sleep(1)
        print(f"done {i}")


async def main() -> None:
    print(f"started at {time.strftime('%X')}")

    # initial_value 管“现在有多少张票”，max_value 管“最多允许还回多少张票”。它主要不是限并发用的，而是防止你把 semaphore 释放过头，顺手把并发限制搞成空气。
    # max_value 用来限制 semaphore 的值最多能涨到多少。
    # 一般要求：
    #   max_value >= initial_value
    sem = anyio.Semaphore(4)

    async with anyio.create_task_group() as task_group:
        for i in range(10):
            task_group.start_soon(expensive, i, sem)

    print(f"finished at {time.strftime('%X')}")

    # started at 20:58:02
    # start 0
    # start 1
    # start 2
    # start 3
    # done 0
    # done 1
    # done 2
    # done 3
    # start 4
    # start 5
    # start 6
    # start 7
    # done 4
    # done 5
    # done 6
    # done 7
    # start 8
    # start 9
    # done 8
    # done 9
    # finished at 20:58:05
    # 用时 3 秒，说明同一时间最多只有 4 个任务在执行 expensive()，达到了限制的目的


if __name__ == "__main__":
    anyio.run(main)
