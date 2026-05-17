# asyncio.set_event_loop(loop)
# 把某个 loop 设置为 当前 OS 线程的当前事件循环。

# 注意：这是 按线程保存的。你在主线程 set 的 loop，子线程里拿不到。官方文档说它会把 loop 设置为当前 OS 线程的 current event loop。
# 这类场景是典型用途：在线程里手动创建一个事件循环，并把它绑定到当前线程。


import time
import asyncio
import threading


async def worker(delay: float) -> None:
    await asyncio.sleep(3)
    print("worker done")


# loop.create_task(worker(1))
# loop.run_forever()
# 含义:
#   先往 loop 里放一个后台任务
#   然后让 loop 一直运行
#   直到有人调用 loop.stop()
# 特点:
#   loop 没有特定等待目标
#   worker 只是 loop 里的一个任务
#   如果 worker 结束了，loop 仍然会继续跑
#   如果以后还要往 loop 里提交别的任务，也可以继续提交
#   适合后台线程里的长期事件循环

# run_until_complete(worker(1))
# 含义:
#   运行事件循环，直到 worker(1) 这个 coroutine 完成, 之后就停止事件循环


def thread_main(loop: asyncio.AbstractEventLoop) -> None:
    asyncio.set_event_loop(loop)

    # 把 worker(1) 创建成 Task，并挂到这个 loop 上
    # loop.create_task(worker(1))
    # 这里不能用
    # asyncio.create_task(worker(1))

    try:
        # loop.run_forever()
        loop.run_until_complete(worker(1))
        print("after")
    finally:
        loop.close()


loop = asyncio.new_event_loop()
t = threading.Thread(target=thread_main, args=(loop,))
t.start()

try:
    while True:
        print("main thread")
        time.sleep(2)
except KeyboardInterrupt:
    print("stopping")

    loop.call_soon_threadsafe(loop.stop)
    t.join()

# main thread
# work 1 seconds
# main thread
# work 2 seconds
# work 3 seconds
# main thread
# work 4 seconds
# work 5 seconds
# main thread
# work 6 seconds
# work 7 seconds
# main thread
