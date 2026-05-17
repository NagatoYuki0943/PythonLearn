# 一个实战模板：并发请求 + 限流 + 超时


from collections.abc import Iterable
import trio


async def ask_one(
    i: int, question: str, limiter: trio.CapacityLimiter, results: dict[int, str]
) -> None:
    async with limiter:
        with trio.fail_after(10):
            await trio.sleep(1)
            results[i] = f"answer to {question}"


async def ask_all(inputs: Iterable[str], concurrency: int = 4) -> list[str]:
    limiter = trio.CapacityLimiter(concurrency)
    results: dict[int, str] = {}

    async with trio.open_nursery() as nursery:
        for i, question in enumerate(inputs):
            nursery.start_soon(ask_one, i, question, limiter, results)

    return [results[i] for i in sorted(results)]


async def main() -> None:
    answers = await ask_all(["a", "b", "c", "d", "e"], concurrency=4)
    print(answers)
    # ['answer to a', 'answer to b', 'answer to c', 'answer to d', 'answer to e']


if __name__ == "__main__":
    trio.run(main)
