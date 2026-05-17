# Trio 的核心是 nursery。nursery.start_soon() 不是 async 函数，不需要 await；它启动子任务后立即返回，而退出 nursery 时会等待所有子任务完成。
# 这点和 asyncio.TaskGroup 很像，但 Trio 是从设计一开始就围绕这套模型来的，不像 asyncio 是后来慢慢补上“别把任务孤儿化”的护栏。
# start_soon 类似 create_task，但它不返回 Task 对象。


import time
import trio


async def worker(i: int, delay: float, results: list[str | None]) -> None:
    await trio.sleep(delay)
    print(f"worker-{i} done after {delay} seconds")
    results[i] = f"result-{i}"


async def main() -> None:
    print(f"started at {time.strftime('%X')}")

    delays = [2, 1, 3, 5, 4]
    results: list[str | None] = [None] * len(delays)

    async with trio.open_nursery() as nursery:
        for i, delay in enumerate(delays):
            # start_soon() 不会等待 worker 执行完成。它的意思是
            #   把这个 async 函数作为子任务启动
            #   然后我自己马上继续往下走
            nursery.start_soon(worker, i, delay, results)

        # 这里 main() 函数挂起了, 把控制权交还给 event loop, 于是 event loop 就可以调度 task1 和 task2 这两个任务了
        await trio.sleep(5)

    print(results)

    print(f"finished at {time.strftime('%X')}")

    # started at 19:07:44
    # worker-1 done after 1 seconds
    # worker-0 done after 2 seconds
    # worker-2 done after 3 seconds
    # worker-4 done after 4 seconds
    # worker-3 done after 5 seconds
    # ['result-0', 'result-1', 'result-2', 'result-3', 'result-4']
    # finished at 19:07:49
    # 相差5秒, 实现了并发


if __name__ == "__main__":
    trio.run(main)
