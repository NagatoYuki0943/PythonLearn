# AnyIO 文档明确说明 task group 有自己的 cancel scope，取消这个 scope 会取消所有子任务。


import time
import anyio


async def worker(name: str) -> None:
    while True:
        print(name)
        await anyio.sleep(1)


# main
#  │
#  ├─ anyio.run(main)
#  │
#  ├─ 进入 main()
#  │
#  │
#  ├─ async with anyio.create_task_group() as task_group
#  │    │
#  │    ├─ 创建 task_group
#  │    │
#  │    ├─ task_group.start_soon(worker, "A")
#  │    │    │
#  │    │    └─ 子任务 A 启动
#  │    │         │
#  │    │         ├─ print("A")
#  │    │         ├─ await anyio.sleep(1)
#  │    │         ...
#  │    │
#  │    ├─ task_group.start_soon(worker, "B")
#  │    │    │
#  │    │    └─ 子任务 B 启动
#  │    │         │
#  │    │         ├─ print("B")
#  │    │         ├─ await anyio.sleep(1)
#  │    │         ...
#  │    │
#  │    ├─ main 执行 await anyio.sleep(3)
#  │    │    │
#  │    │    └─ main 挂起 3 秒，把执行权让给 A / B
#  │    │
#  │    ├─ 3 秒后 main 恢复
#  │    │
#  │    ├─ task_group.cancel_scope.cancel()
#  │    │    │
#  │    │    ├─ 请求取消子任务 A
#  │    │    └─ 请求取消子任务 B
#  │    │
#  │    ├─ A 在 await anyio.sleep(1) 处收到取消并退出
#  │    │
#  │    ├─ B 在 await anyio.sleep(1) 处收到取消并退出
#  │    │
#  │    └─ task_group 确认所有子任务结束
#  │
#  ├─ 退出 async with task_group
#  │
#  └─ main 结束
async def main() -> None:
    print(f"started at {time.strftime('%X')}")

    async with anyio.create_task_group() as task_group:
        # start_soon() 不会等待 worker 执行完成。它的意思是
        #   把这个 async 函数作为子任务启动
        #   然后我自己马上继续往下走
        task_group.start_soon(worker, "A")
        task_group.start_soon(worker, "B")

        # 此时 main 挂起，A 和 B 两个 worker 开始运行
        await anyio.sleep(3)
        # 3 秒后 main 恢复，取消 task group 里的子任务 A 和 B
        task_group.cancel_scope.cancel()

    print(f"finished at {time.strftime('%X')}")

    # started at 20:52:22
    # A
    # B
    # A
    # B
    # A
    # B
    # finished at 20:52:25


if __name__ == "__main__":
    anyio.run(main)
