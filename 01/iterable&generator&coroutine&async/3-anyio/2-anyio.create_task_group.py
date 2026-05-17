# AnyIO 的任务模型跟 Trio 很像：通过 task group 创建任务，退出上下文时保证子任务已经结束；如果子任务或上下文里的代码抛异常，所有子任务会被取消。
# AnyIO 4 里要注意：TaskGroup.start_soon() 是同步方法，不要 await task_group.start_soon(...)。老写法 spawn() 已经是远古化石了，别挖。


import time
import anyio


async def worker(i: int, delay: float, results: list[str | None]) -> None:
    await anyio.sleep(delay)
    print(f"worker-{i} done after {delay} seconds")
    results[i] = f"result-{i}"


async def main() -> None:
    print(f"started at {time.strftime('%X')}")

    delays = [2, 1, 3, 5, 4]
    results: list[str | None] = [None] * len(delays)

    async with anyio.create_task_group() as task_group:
        for i, delay in enumerate(delays):
            # start_soon() 不会等待 worker 执行完成。它的意思是
            #   把这个 async 函数作为子任务启动
            #   然后我自己马上继续往下走
            task_group.start_soon(worker, i, delay, results)

        # 这里 main() 函数挂起了, 把控制权交还给 event loop, 于是 event loop 就可以调度 task1 和 task2 这两个任务了
        await anyio.sleep(5)

    print(results)

    print(f"finished at {time.strftime('%X')}")

    # started at 20:45:34
    # worker-1 done after 1 seconds
    # worker-0 done after 2 seconds
    # worker-2 done after 3 seconds
    # worker-4 done after 4 seconds
    # worker-3 done after 5 seconds
    # ['result-0', 'result-1', 'result-2', 'result-3', 'result-4']
    # finished at 20:45:39
    # 相差5秒, 实现了并发


if __name__ == "__main__":
    anyio.run(main)
