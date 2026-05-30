# 如果线程不是 AnyIO 创建的外部线程，需要 event loop token 或 BlockingPortal。


import anyio
from anyio import from_thread, to_thread


async def worker(delay: float) -> None:
    i = 0
    while True:
        await anyio.sleep(delay)
        print(f"work {i + 1} seconds")
        i += 1


def sync_func() -> None:
    # 这个线程是 AnyIO 创建的，所以可以回到事件循环
    from_thread.run(anyio.sleep, 1)
    from_thread.run(worker, 1)


async def main() -> None:
    await to_thread.run_sync(sync_func)


if __name__ == "__main__":
    anyio.run(main)
