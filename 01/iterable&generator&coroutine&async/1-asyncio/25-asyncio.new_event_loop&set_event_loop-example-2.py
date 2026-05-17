# new_event_loop, set_event_loop, get_running_loop 现代场景

# 场景1:
# 你在子线程里跑 asyncio loop
# 例如你有一个同步主程序，但想在后台线程里维护一个 asyncio loop


import asyncio
import threading


async def coro():
    await asyncio.sleep(1)
    return "hello"


def loop_thread(loop: asyncio.AbstractEventLoop):
    asyncio.set_event_loop(loop)
    loop.run_forever()


loop = asyncio.new_event_loop()
thread = threading.Thread(target=loop_thread, args=(loop,), daemon=True)
thread.start()

future = asyncio.run_coroutine_threadsafe(coro(), loop)
print(future.result())

loop.call_soon_threadsafe(loop.stop)
thread.join()
loop.close()

# 这里的逻辑是：
#   loop = asyncio.new_event_loop()
#   asyncio.set_event_loop(loop)
#   loop.run_forever()
# run_coroutine_threadsafe() 则用来从别的线程往这个 loop 里提交 coroutine。这个场景还是有现实意义的，比如 GUI 程序、同步 SDK 包异步客户端、老项目渐进迁移。也就是异步世界和同步世界被迫联姻，祝它们幸福。
