# create_memory_object_stream 缓冲流。
# create_memory_object_stream(0) 是无缓冲流，发送方会等接收方接收，这会形成天然背压；无限缓冲虽然看起来省事，但生产快于消费时会堆积内存和延迟，经典“先欠着，以后再还”，听起来像技术债的亲戚。


import anyio
from anyio.abc import ObjectSendStream, ObjectReceiveStream


async def producer(send: ObjectSendStream[int], num: int) -> None:
    async with send:
        for i in range(num):
            print("sending", i)
            await send.send(i)
            await anyio.sleep(0.5)


async def consumer(receive: ObjectReceiveStream[int]) -> None:
    async with receive:
        async for item in receive:
            print("got", item)
            await anyio.sleep(1)


async def main() -> None:
    send, receive = anyio.create_memory_object_stream[int](2)

    async with anyio.create_task_group() as task_group:
        task_group.start_soon(producer, send, 5)
        task_group.start_soon(consumer, receive)

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
    anyio.run(main)
