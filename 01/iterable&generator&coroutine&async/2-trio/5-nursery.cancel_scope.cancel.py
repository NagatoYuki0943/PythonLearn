# nursery 自带 cancel_scope，取消它会取消其子任务。
# Trio 的取消是 “level-triggered”，已经取消的作用域里，后续可取消操作会继续触发取消，这能避免某些清理逻辑里“取消只响一次，然后程序挂住”的坑。


import time
import trio


async def worker(name: str) -> None:
    while True:
        print(name)
        await trio.sleep(1)


# main
#  │
#  ├─ trio.run(main)
#  │
#  ├─ 进入 main()
#  │
#  │
#  ├─ async with trio.open_nursery() as nursery
#  │    │
#  │    ├─ 创建 nursery
#  │    │
#  │    ├─ nursery.start_soon(worker, "A")
#  │    │    │
#  │    │    └─ 子任务 A 启动
#  │    │         │
#  │    │         ├─ print("A")
#  │    │         ├─ await trio.sleep(1)
#  │    │         ...
#  │    │
#  │    ├─ nursery.start_soon(worker, "B")
#  │    │    │
#  │    │    └─ 子任务 B 启动
#  │    │         │
#  │    │         ├─ print("B")
#  │    │         ├─ await trio.sleep(1)
#  │    │         ...
#  │    │
#  │    ├─ main 执行 await trio.sleep(3)
#  │    │    │
#  │    │    └─ main 挂起 3 秒，把执行权让给 A / B
#  │    │
#  │    ├─ 3 秒后 main 恢复
#  │    │
#  │    ├─ nursery.cancel_scope.cancel()
#  │    │    │
#  │    │    ├─ 请求取消子任务 A
#  │    │    └─ 请求取消子任务 B
#  │    │
#  │    ├─ A 在 await trio.sleep(1) 处收到取消并退出
#  │    │
#  │    ├─ B 在 await trio.sleep(1) 处收到取消并退出
#  │    │
#  │    └─ nursery 确认所有子任务结束
#  │
#  ├─ 退出 async with nursery
#  │
#  └─ main 结束
async def main() -> None:
    print(f"started at {time.strftime('%X')}")

    async with trio.open_nursery() as nursery:
        # start_soon() 不会等待 worker 执行完成。它的意思是
        #   把这个 async 函数作为子任务启动
        #   然后我自己马上继续往下走
        nursery.start_soon(worker, "A")
        nursery.start_soon(worker, "B")

        # 此时 main 挂起，A 和 B 两个 worker 开始运行
        await trio.sleep(3)
        # 3 秒后 main 恢复，取消 nursery 里的子任务 A 和 B
        nursery.cancel_scope.cancel()

    print(f"finished at {time.strftime('%X')}")

    # started at 20:52:09
    # B
    # A
    # B
    # A
    # B
    # A
    # finished at 20:52:12


if __name__ == "__main__":
    trio.run(main)
