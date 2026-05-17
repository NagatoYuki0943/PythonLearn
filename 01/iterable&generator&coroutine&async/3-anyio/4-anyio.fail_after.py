# fail_after() 和 move_on_after() 类似，但超时后会抛出 TimeoutError，适合“超时就是失败”的逻辑。


import anyio


async def main() -> None:

    try:
        with anyio.fail_after(2):
            await anyio.sleep(10)
    except TimeoutError:
        print("too slow")
    # too slow


if __name__ == "__main__":
    anyio.run(main)
