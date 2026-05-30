# 这个模式和 Semaphore 的区别
# Semaphore：适合“一次性任务列表”
#   一开始创建 20 个 task
#   但最多 4 个进入 sem 内部执行
# Queue + worker：适合“生产者-消费者”
# 适合：
#   任务很多；
#   任务不断产生；
#   要做 pipeline；
#   要控制内存；
#   要生产者和消费者解耦。
# 如果任务数量特别大，比如几十万，Queue + worker 通常比创建几十万个 task 更稳。毕竟不是每个任务都非得变成一个 task，人类已经创造了够多对象了.


import time
import asyncio


async def worker(name: str, queue: asyncio.Queue[int]) -> None:
    try:
        while True:
            # 从队列里取一个元素。
            # 如果队列里有东西，它立刻返回。
            # 如果队列空了，它会挂起当前 worker，直到队列里又有新元素。
            item = await queue.get()
            try:
                print(f"{name} processing {item}")
                # 当前 worker 暂停 1 秒
                # 把控制权交还给事件循环
                # 1 秒后再恢复这个 worker
                await asyncio.sleep(1)
            finally:
                # asyncio.Queue 未完成任务数 -1。
                queue.task_done()
    except asyncio.CancelledError:
        print(f"{name} cancelled")
        raise


# main
#  │
#  ├─ started
#  │
#  ├─ 创建 queue
#  │
#  ├─ put 0~19
#  │
#  ├─ 创建 4 个 worker task
#  │
#  ├─ await queue.join()
#  │    │
#  │    ├─ worker-0: get 0 -> sleep 1s -> task_done
#  │    ├─ worker-1: get 1 -> sleep 1s -> task_done
#  │    ├─ worker-2: get 2 -> sleep 1s -> task_done
#  │    ├─ worker-3: get 3 -> sleep 1s -> task_done
#  │    │
#  │    ├─ 重复消费，直到 20 个任务全部 task_done
#  │
#  ├─ cancel 4 个 worker
#  │
#  ├─ gather 回收取消异常
#  │
#  └─ finished
async def main() -> None:
    print(f"started at {time.strftime('%X')}")

    # 创建一个队列
    # asyncio.Queue 内部会维护一个未完成任务计数器。
    # 这里没有设置 maxsize，默认是无限大的，如果设置了 maxsize 且小于 20，那么下面的 put 部分就会阻塞。
    queue: asyncio.Queue[int] = asyncio.Queue()

    # 往里面放 20 个任务
    for i in range(20):
        # asyncio.Queue 未完成任务数 +1。
        await queue.put(i)

    # 创建 4 个 worker 消费队列
    workers = [asyncio.create_task(worker(f"worker-{i}", queue)) for i in range(4)]

    # asyncio.Queue 未完成任务数归零后，queue.join() 解除阻塞
    # 等待队列里的任务全部被处理完
    await queue.join()

    # 取消 4 个无限循环 worker
    for task in workers:
        task.cancel()

    # 回收 worker task 取消异常
    await asyncio.gather(*workers, return_exceptions=True)

    print(f"finished at {time.strftime('%X')}")

    # started at 18:20:48
    # worker-0 processing 0
    # worker-1 processing 1
    # worker-2 processing 2
    # worker-3 processing 3
    # worker-0 processing 4
    # worker-1 processing 5
    # worker-2 processing 6
    # worker-3 processing 7
    # worker-0 processing 8
    # worker-1 processing 9
    # worker-2 processing 10
    # worker-3 processing 11
    # worker-0 processing 12
    # worker-1 processing 13
    # worker-2 processing 14
    # worker-3 processing 15
    # worker-0 processing 16
    # worker-1 processing 17
    # worker-2 processing 18
    # worker-3 processing 19
    # worker-0 cancelled
    # worker-1 cancelled
    # worker-2 cancelled
    # worker-3 cancelled
    # finished at 18:20:53
    # 相差5秒, 实现了并发, 同时运行的 task 最多只有 4 个


if __name__ == "__main__":
    asyncio.run(main())
