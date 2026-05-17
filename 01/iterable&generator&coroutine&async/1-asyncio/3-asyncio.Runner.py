# Runner 适合在同步上下文里多次调用顶层 async 函数，并共享同一个事件循环和 contextvars.Context。
# 平时脚本一个 asyncio.run(main()) 就够了，不需要为了显得高级把代码写成宗教仪式。


import time
import asyncio


async def init() -> str:
    await asyncio.sleep(1)
    return "ready"


async def work() -> None:
    await asyncio.sleep(2)
    print("working")


with asyncio.Runner() as runner:
    print(f"started at {time.strftime('%X')}")
    status = runner.run(init())
    print(status)
    runner.run(work())
    print(f"finished at {time.strftime('%X')}")

    # started at 17:22:44
    # ready
    # working
    # finished at 17:22:47
    # 相差3秒, 没有实现并发
