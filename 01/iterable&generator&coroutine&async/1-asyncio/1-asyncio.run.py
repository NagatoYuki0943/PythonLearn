# asyncio.run() 是运行顶层 async 程序的推荐入口，它会创建事件循环、运行 awaitable、清理异步生成器和默认 executor；
# 但它不能在同一个线程已有事件循环运行时再调用，比如 Jupyter 里通常应该直接 await main()，不要在 loop 里套 loop，套娃这种东西留给俄罗斯纪念品就行。

# Python 3.14 里 asyncio.run() 和 Runner.run() 都允许传入任意 awaitable，不再只限 coroutine；同时事件循环 policy 系统已被标记为将来移除，配置 loop 更推荐用 loop_factory。


import asyncio


# async def func() 是一个 coroutine function
# 调用它时返回一个 coroutine object
# 不会运行函数里面的代码
async def main() -> None:
    print("hello")
    # asyncio.sleep() 会挂起当前协程，把控制权交还给事件循环；
    # 当前任务会在 delay 秒后恢复执行。
    await asyncio.sleep(1)
    print("world")


if __name__ == "__main__":
    coro = main()  # coro 是一个 coroutine object
    print(coro)
    asyncio.run(coro)
    # <coroutine object main at 0x000001A325C46B00>
    # hello
    # world
