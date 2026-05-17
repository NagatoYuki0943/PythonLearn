# fail_after() 和 move_on_after() 类似，但超时后会抛出 TooSlowError，适合“超时就是失败”的逻辑。


import trio


async def main() -> None:
    try:
        with trio.fail_after(2):
            await trio.sleep(10)
    except trio.TooSlowError:
        print("too slow")
    # too slow


if __name__ == "__main__":
    trio.run(main)
