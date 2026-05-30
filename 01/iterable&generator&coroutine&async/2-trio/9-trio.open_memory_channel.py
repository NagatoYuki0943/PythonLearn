# open_memory_channel 缓冲通道。
# open_memory_channel(0) 是无缓冲通道，发送方会等接收方接收，这会形成天然背压；无限缓冲虽然看起来省事，但生产快于消费时会堆积内存和延迟，经典“先欠着，以后再还”，听起来像技术债的亲戚。


import trio


async def producer(send: trio.MemorySendChannel[int], num: int) -> None:
    async with send:
        for i in range(num):
            print("sending", i)
            await send.send(i)
            await trio.sleep(0.5)


async def consumer(receive: trio.MemoryReceiveChannel[int]) -> None:
    async with receive:
        async for item in receive:
            print("got", item)
            await trio.sleep(1)


async def main() -> None:
    send, receive = trio.open_memory_channel[int](2)

    async with trio.open_nursery() as nursery:
        nursery.start_soon(producer, send, 5)
        nursery.start_soon(consumer, receive)

    # sending 0
    # got 0
    # sending 1
    # sending 2
    # got 1
    # sending 3
    # sending 4
    # got 2
    # got 3
    # got 4


if __name__ == "__main__":
    trio.run(main)
