import asyncio
import time


async def say_after(delay, what):
    # asyncio.sleep() 会阻塞当前协程, 直到 delay 秒后才继续执行
    await asyncio.sleep(delay)
    return f"{what} - {delay} seconds"


async def main():
    # create_task() 会把 coroutine 转换为一个 task 对象, 并将其注册到 event loop
    # 但是 event loop 并不会立即执行该 task, 以为当前控制权仍在 main() 函数中
    # main() 函数会继续创建另一个 task 对象, 并注册到 event loop
    task1 = asyncio.create_task(say_after(1, "hello"))
    task2 = asyncio.create_task(say_after(2, "world"))

    print(f"started at {time.strftime('%X')}")

    # 1. await 后面是一个 task 对象, 是告诉 event loop 等待该 task 执行完毕
    # 2. 然后把控制权交给了 event loop, 直到该 task 执行完毕, 才会继续执行下面的代码
    # 3. 然后 main() 函数会 await 另一个 task 对象, 2个 task 并行执行, 并等待其执行完毕
    ret1 = await task1
    ret2 = await task2

    print(ret1)
    print(ret2)

    print(f"finished at {time.strftime('%X')}")

    # started at 13:10:55
    # hello - 1 seconds
    # world - 2 seconds
    # finished at 13:10:57
    # 相差2秒, 实现并行


asyncio.run(main())
