import asyncio
import time

async def say_after(delay, what):
    # asyncio.sleep() 会阻塞当前协程, 直到 delay 秒后才继续执行
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")

    # coroutine 可以理解为一个生成器
    # 1. await 不会把 coroutine 转换为 task, 只是调用生成器, 同步执行, 直到遇到无法继续执行的情况, 如 await asyncio.sleep(1) 会 yield 出去, 告诉 event loop 这个 task 干不了了, 让其他 task 去执行
    # 2. 同时会在那个 task 或者 future 中标记一下(回调函数), 让依赖的那个 task 或者 future 完成后, 来执行这个 task
    #    可以理解为 main() await 了 say_after(), 在 say_after() 中添加了一个回调函数, say_after() 完成后, 才会执行 main() 的下一行代码
    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")

    # started at 12:54:41
    # hello
    # world
    # finished at 12:54:44
    # 相差3秒, 没有实现并行

asyncio.run(main())
