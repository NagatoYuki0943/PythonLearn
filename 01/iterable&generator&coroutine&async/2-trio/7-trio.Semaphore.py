# CapacityLimiter 用来限制同一时间访问某种资源的任务数量，比如最多同时 4 个请求、最多 40 个线程任务等；
# Trio 文档也把它描述为控制有限容量资源访问的工具。


import time
import trio


async def expensive(i: int, sem: trio.Semaphore) -> None:
    async with sem:
        print(f"start {i}")
        await trio.sleep(1)
        print(f"done {i}")


async def main() -> None:
    print(f"started at {time.strftime('%X')}")

    # initial_value 管“现在有多少张票”，max_value 管“最多允许还回多少张票”。它主要不是限并发用的，而是防止你把 semaphore 释放过头，顺手把并发限制搞成空气。
    # max_value 用来限制 semaphore 的值最多能涨到多少。
    # 一般要求：
    #   max_value >= initial_value
    sem = trio.Semaphore(4)

    async with trio.open_nursery() as nursery:
        for i in range(10):
            nursery.start_soon(expensive, i, sem)

    print(f"finished at {time.strftime('%X')}")

    # started at 19:33:48
    # start 3
    # start 2
    # start 1
    # start 0
    # done 0
    # done 1
    # done 2
    # done 3
    # start 7
    # start 6
    # start 5
    # start 4
    # done 7
    # done 6
    # done 5
    # done 4
    # start 9
    # start 8
    # done 8
    # done 9
    # finished at 19:33:51
    # 用时 3 秒，说明同一时间最多只有 4 个任务在执行 expensive()，达到了限制的目的


if __name__ == "__main__":
    trio.run(main)
