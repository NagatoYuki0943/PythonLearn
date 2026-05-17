# AnyIO 可以运行在 asyncio 或 Trio 后端上，代码通常不需要改；这很适合写库，或者你想要 Trio 风格的结构化并发，但项目实际跑在 asyncio 生态里。


import anyio


async def main() -> None:
    print("hello")
    await anyio.sleep(1)
    print("world")


if __name__ == "__main__":
    anyio.run(main)
    # 指定后端：
    # anyio.run(main, backend="asyncio")
    # 或
    # anyio.run(main, backend="trio")
