# 一个实战模板：并发请求 + 限流 + 超时


from collections.abc import Iterable
import asyncio


async def ask_one(i: int, question: str, sem: asyncio.Semaphore) -> tuple[int, str]:
    async with sem:
        async with asyncio.timeout(10):
            # 模拟请求 LLM / HTTP API
            await asyncio.sleep(1)
            return i, f"answer to {question}"


async def ask_all(inputs: Iterable[str], concurrency: int = 4) -> list[str]:
    sem = asyncio.Semaphore(concurrency)
    tasks: list[asyncio.Task[tuple[int, str]]] = []

    async with asyncio.TaskGroup() as task_group:
        for i, question in enumerate(inputs):
            task = task_group.create_task(ask_one(i, question, sem))
            tasks.append(task)

    results = [task.result() for task in tasks]
    results.sort(key=lambda x: x[0])
    return [answer for _, answer in results]


async def main() -> None:
    answers = await ask_all(["a", "b", "c", "d", "e"], concurrency=4)
    print(answers)
    # ['answer to a', 'answer to b', 'answer to c', 'answer to d', 'answer to e']


if __name__ == "__main__":
    asyncio.run(main())
