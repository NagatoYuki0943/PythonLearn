# semaphore 是 信号量，作用是限制同时运行的异步请求数量


import time
import asyncio


async def request(i: int, sem: asyncio.Semaphore) -> str:
    async with sem:
        print(f"start {i}")
        await asyncio.sleep(1)
        print(f"done {i}")
        return f"result-{i}"


async def main() -> None:
    # 这里即使一次创建了 10 个 task，真正进入 async with sem: 的最多只有 4 个。也就是你之前问的那种写法：只要所有任务共享同一个 semaphore，对并发限制就有效，不是放在 ask_one() 里面就失效。

    print(f"started at {time.strftime('%X')}")

    sem = asyncio.Semaphore(4)

    async with asyncio.TaskGroup() as task_group:
        tasks = [task_group.create_task(request(i, sem)) for i in range(10)]

    print([t.result() for t in tasks])

    print(f"finished at {time.strftime('%X')}")

    # started at 18:02:11
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
    # ['result-0', 'result-1', 'result-2', 'result-3', 'result-4', 'result-5', 'result-6', 'result-7', 'result-8', 'result-9']
    # finished at 18:02:14
    # 相差3秒, 实现了并发, 但是同时运行的 task 最多只有 4 个


if __name__ == "__main__":
    asyncio.run(main())
