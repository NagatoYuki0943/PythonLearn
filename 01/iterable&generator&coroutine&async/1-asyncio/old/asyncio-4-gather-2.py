import asyncio
import time


async def say_after(delay, what):
    # asyncio.sleep() 会阻塞当前协程, 直到 delay 秒后才继续执行
    await asyncio.sleep(delay)
    return f"{what} - {delay} seconds"


async def main():
    print(f"started at {time.strftime('%X')}")

    # asyncio.gather() 返回一个 future 对象
    # gather() 参数时若干个 coroutine 或 task 或 future 对象, 它会等待所有参数都执行完毕后才返回结果
    # 返回结果是一个列表, 列表中的元素顺序与参数顺序一致
    ret = await asyncio.gather(say_after(1, "hello"), say_after(2, "world"))

    print(ret)

    print(f"finished at {time.strftime('%X')}")

    # started at 13:17:11
    # ['hello - 1 seconds', 'world - 2 seconds']
    # finished at 13:17:13
    # 相差2秒, 实现并行


asyncio.run(main())
