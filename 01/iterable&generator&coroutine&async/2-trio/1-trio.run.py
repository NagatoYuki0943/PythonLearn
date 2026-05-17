# Trio 的入口是 trio.run(async_fn, *args)，必须从同步上下文调用；几乎所有 Trio API 都要求已经处在 trio.run() 内部。


import trio


async def main() -> None:
    print("hello")
    await trio.sleep(1)
    print("world")


if __name__ == "__main__":
    trio.run(main)
