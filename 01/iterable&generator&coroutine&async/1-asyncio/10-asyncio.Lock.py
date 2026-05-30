# asyncio.Lock 是给 asyncio tasks 用的 mutex，不是线程安全的。
# asyncio 还提供 Event、Condition、Semaphore、BoundedSemaphore、Barrier 等同步原语。

import asyncio


counter = 0
lock = asyncio.Lock()


async def worker():
    global counter

    async with lock:
        old = counter
        await asyncio.sleep(0.01)
        counter = old + 1


async def main():
    await asyncio.gather(*(worker() for _ in range(100)))
    print(counter)


if __name__ == "__main__":
    asyncio.run(main())
