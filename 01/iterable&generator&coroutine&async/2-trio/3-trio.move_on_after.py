# move_on_after() 会创建一个取消作用域，超时后取消作用域内的操作，并吞掉取消异常；可以通过 cancelled_caught 判断是否发生了超时。


import trio


async def main() -> None:
    with trio.move_on_after(2) as cancel_scope:
        await trio.sleep(10)
        print("finished")

    if cancel_scope.cancelled_caught:
        print("timed out, but continue")

    # timed out, but continue


if __name__ == "__main__":
    trio.run(main)
