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
    task1 = asyncio.create_task(say_after(1, 'hello'))
    task2 = asyncio.create_task(say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    # asyncio.gather() 返回一个 future 对象
    # gather() 参数时若干个 coroutine 或 task 或 future 对象, 它会等待所有参数都执行完毕后才返回结果
    # 返回结果是一个列表, 列表中的元素顺序与参数顺序一致
    ret = await asyncio.gather(task1, task2)

    print(ret)

    print(f"finished at {time.strftime('%X')}")

    # started at 13:16:55
    # ['hello - 1 seconds', 'world - 2 seconds']
    # finished at 13:16:57
    # 相差2秒, 实现并行

asyncio.run(main())
