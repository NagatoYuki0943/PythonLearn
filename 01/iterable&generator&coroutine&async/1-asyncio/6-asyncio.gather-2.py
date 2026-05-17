# gather() 适合“并发跑一组任务并收集返回值”的简单场景；
# 但如果你希望某个任务炸了以后整个任务组一起取消，优先用 TaskGroup。
# gather(return_exceptions=True) 会把异常当作结果返回，这在批处理里有用，但也很容易让错误被安详地埋葬。


import time
from typing import Any
import asyncio


async def say_after(delay: float, what: Any):
    # asyncio.sleep() 会挂起当前协程，把控制权交还给事件循环；
    # 当前任务会在 delay 秒后恢复执行。
    await asyncio.sleep(delay)
    print(f"{what} - {delay} seconds")
    return f"{what} - {delay} seconds"


async def main():
    print(f"started at {time.strftime('%X')}")

    coro1 = say_after(2, "hello")
    coro2 = say_after(1, "world")

    # asyncio.gather() 返回一个 future 对象
    # gather() 参数时若干个 coroutine 或 task 或 future 对象, 它会等待所有参数都执行完毕后才返回结果
    # 返回结果是一个列表, 列表中的元素顺序与参数顺序一致
    ret = await asyncio.gather(coro1, coro2)

    print(ret)

    print(f"finished at {time.strftime('%X')}")

    # started at 17:35:35
    # ['hello - 2 seconds', 'world - 1 seconds']
    # finished at 17:35:37
    # 相差2秒, 实现并发


if __name__ == "__main__":
    asyncio.run(main())
