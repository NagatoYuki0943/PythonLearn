# 取消任务：task.cancel
# 被取消时通常会在下一个 await 点抛出 CancelledError。如果捕获取消异常，清理完应该重新 raise，否则任务可能表现得像“我没死，我只是拒绝承认现实”。


import asyncio


async def job() -> None:
    try:
        while True:
            print("working")
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        print("cleanup")
        # 重新把取消异常抛出去。
        # 外面的 await task 收到 CancelledError，就知道这个 task 是被取消了的。
        raise


# main:
#   create_task(job)
#   await sleep(3)  ────────────────┐
#                                   │ main 挂起，job 得以运行
# job:                              │
#   print working                   │
#   await sleep(1)                  │
#   print working                   │
#   await sleep(1)                  │
#   print working                   │
#   await sleep(1)                  │
#                                   │
# main recovery                     │
#   task.cancel()                   │
#                                   │
# job 在 await sleep(1) 处收到取消异常
#   except CancelledError
#   print cleanup
#   raise
#                                   │
# main:
#   await task 收到 CancelledError
#   print cancelled
async def main() -> None:
    # 这句做了两件事：
    # 创建 job() 这个 coroutine；
    # 把它包装成 Task，交给事件循环调度。
    # 只是创建 coroutine 对象，不会马上完整执行。
    task = asyncio.create_task(job())

    # 让当前协程 main() 暂停 3 秒，把控制权交还给事件循环。
    # 于是事件循环一看：
    #   main 暂时睡了
    #   job 这个 task 可以跑
    # 然后就开始运行 job()。
    await asyncio.sleep(3)

    # 给这个 task 发一个取消请求。
    #   然后 asyncio 会在这个 task 下次恢复执行时，向它里面注入一个异常：asyncio.CancelledError
    task.cancel()

    try:
        # 很多人以为：task.cancel() 之后就完事了。
        # 其实 task.cancel() 只是发出取消请求。
        # 还需要：await task 等待这个 task 真正走完取消流程。
        await task
    except asyncio.CancelledError:
        print("cancelled")

    # working
    # working
    # working
    # cleanup
    # cancelled


if __name__ == "__main__":
    asyncio.run(main())
