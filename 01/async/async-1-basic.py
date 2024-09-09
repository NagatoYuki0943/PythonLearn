import asyncio
import time


# async def func() 是一个 coroutine function
# 调用它时返回一个 coroutine object
# 不会运行函数里面的代码
async def main():
    print("Hello")
    await asyncio.sleep(1)
    print("world")

coro = main()
print(coro)
# <coroutine object main at 0x000001FE7EFCD3C0>

# 运行 coroutine object, 传入一个 coroutine object, 把它变成一个 task
# 并把 task 放到 event loop 里
asyncio.run(coro)
