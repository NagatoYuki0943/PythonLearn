# 超时：优先 asyncio.timeout()

# asyncio.timeout() 是异步上下文管理器，用来限制一段 async 代码的等待时间；
# 超时后它会取消当前任务，并把内部的 CancelledError 转换为外部可捕获的 TimeoutError。
# 注意 TimeoutError 要在 async with 外面捕获，人类又一次被缩进支配。


import asyncio


async def slow_request() -> str:
    await asyncio.sleep(10)
    return "ok"


async def main() -> None:
    try:
        async with asyncio.timeout(2):
            result = await slow_request()
            print(result)
    except TimeoutError:
        print("timeout")


if __name__ == "__main__":
    asyncio.run(main())
