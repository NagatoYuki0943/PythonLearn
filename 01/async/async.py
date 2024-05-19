"""https://kimi.moonshot.cn/chat/cp4nrp6aoforkbkld7vg

在 Python 中，异步生成器（AsyncGenerator）与普通的生成器（Generator）类似，
但它们是用于异步迭代的。当你在异步生成器中使用 return 语句时，它的行为与普通生成器略有不同。
return 语句在异步生成器中会抛出一个特殊的 StopAsyncIteration 异常，这可以用来结束生成器的迭代。

如果你在异步生成器中遇到 return 语句的问题，可能是因为你错误地使用了 return 来尝试返回一个值。
在异步生成器中，你不能直接使用 return 来返回一个值，因为它是用来结束生成器的。相反，你应该使用 yield 来产生值。

如果你的协程需要被调用并获取其结果，你应该使用 await 来等待协程完成。

如果你需要从同步代码中启动异步操作，你可以使用 asyncio.run() 来运行顶级的异步函数。
这将创建一个新的事件循环，运行顶级的协程，然后关闭事件循环。请注意，asyncio.run() 只能被调用一次，通常用于启动整个程序。
"""
import asyncio
from typing import AsyncGenerator


async def async_function_a():
    return "this is async_function_a"


async def async_function_b():
    # 如果你的协程需要被调用并获取其结果，你应该使用 await 来等待协程完成。
    result = await async_function_a()
    print(result)


asyncio.run(async_function_b())
# this is async_function_a


#############################################################


async def async_generator_a() -> AsyncGenerator[int, None]:
    for i in range(3):
        yield i  # 使用 yield 来产生值
    return  # 这里用来结束生成器，不返回任何值


# 嵌套调用也要使用 async
async def async_generator_b():
    # AsyncGenerator 需要通过异步迭代来处理，而异步迭代只能通过 async for 循环在异步函数中进行
    async for value in async_generator_a():
        print(value)


# 运行async_generator_b
asyncio.run(async_generator_b())
# 0
# 1
# 2

# 异步主函数，用于运行异步函数 b
async def main():
    # 如果你的协程需要被调用并获取其结果，你应该使用 await 来等待协程完成。
    await async_generator_b()


asyncio.run(main())
# 0
# 1
# 2
