# trio.Lock 是经典 mutex，并且是 非可重入、单所有者锁，只有持有锁的任务能释放它；它也可以作为 async context manager 使用。
# Trio 还有 StrictFIFOLock，用于严格先来先服务的锁场景。


import trio


counter = 0
lock = trio.Lock()


async def worker():
    global counter

    async with lock:
        old = counter
        await trio.sleep(0.01)
        counter = old + 1


async def main():
    async with trio.open_nursery() as nursery:
        for _ in range(100):
            nursery.start_soon(worker)

    print(counter)


if __name__ == "__main__":
    trio.run(main)
