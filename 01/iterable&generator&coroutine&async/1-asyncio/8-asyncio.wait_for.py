# 超时：优先 asyncio.timeout()
# wait_for 是老的写法


import asyncio


async def slow_request() -> str:
    await asyncio.sleep(10)
    return "ok"


async def main() -> None:
    try:
        result = await asyncio.wait_for(slow_request(), timeout=2)
        print(result)
    except TimeoutError:
        print("timeout")


if __name__ == "__main__":
    asyncio.run(main())
