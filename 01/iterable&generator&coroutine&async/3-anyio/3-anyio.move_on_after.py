# AnyIO 的取消模型跟 Trio 一样使用 cancel scopes；task group 自带 cancel scope，可以取消整组任务。
# AnyIO 3 之后 move_on_after() / fail_after() 是普通 with，不是 async with，写错了属于版本迁移时期留下的考古坑。


import anyio


async def main() -> None:
    with anyio.move_on_after(2) as cancel_scope:
        await anyio.sleep(10)
        print("finished")

    if cancel_scope.cancelled_caught:
        print("timed out, but continue")

    # timed out, but continue


if __name__ == "__main__":
    anyio.run(main)
