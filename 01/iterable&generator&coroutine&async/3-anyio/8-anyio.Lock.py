# AnyIO 也有 Lock。官方文档说它用于保护共享资源，确保同一时间只有一个 task 能访问；它类似最大值为 1 的 semaphore，但只有获取锁的 task 能释放它。
# AnyIO 也强调这些同步原语不是线程安全的，不能直接拿去给 worker threads 用。


import anyio


counter = 0
lock = anyio.Lock()


async def worker():
    global counter

    async with lock:
        old = counter
        await anyio.sleep(0.01)
        counter = old + 1


async def main():
    async with anyio.create_task_group() as tg:
        for _ in range(100):
            tg.start_soon(worker)

    print(counter)


if __name__ == "__main__":
    anyio.run(main)
